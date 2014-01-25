"""
een programma om voor de geocache twee zes vier een magisch vierkant
te bepalen waarvoor geldt dat het magisch getal 264 is, het 5 x 5 velden bevat.
De te gebruiken getallen zijn alle 2-cijferige combinaties van de getallen 0, 1, 6, 8 en 9 (met voorloopnul)
Dus 25 getallen
Verder kan het vierkant 180 graden gedraaid worden waarbij de getallen omgekeerd worden gelezen (16 wordt 91)
en is het dan nog steeds een magisch vierkant met het magisch getal 264

"""
import time
import math

# globals
positie = 1
teller = 0
afgewezen = 0
doorloop = 0

oplossing = [89, -1, -1, -1, -1,
             -1, -1, -1, 86, -1,
             16, -1,  0, -1, -1,
             -1, -1, 66, -1, -1,
             -1, 10, -1, -1, 96]

getallen = [1, 6, 8, 9, 11, 18, 19, 60, 61, 68, 69, 80, 81, 88, 90, 91, 98, 99]
pos_in_oplossing = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 17, 19, 20, 21, 23, 24]
inverse = { 0:  0,  1: 10,  6: 90,  8: 80,  9: 60,
           10:  1, 11: 11, 16: 91, 18: 81, 19: 61,
           60:  9, 61: 19, 66: 99, 68: 89, 69: 69,
           80:  8, 81: 18, 86: 98, 88: 88, 89: 68,
           90:  6, 91: 16, 96: 96, 98: 86, 99: 66}

cw = { 'd': 1, 'w': 4, 'y': 10, 'b': 13, 'e': 14, 'a': 15, 'v': 18, 'g': 20, 'x': 23 }

def sum_col (col, oplossing):
    """ (int, list of int) -> int

        Return de optelsom van kolom col uit oplossing (5x5 in list van 25)
        Als een element uit de kolom -1 is dan wordt de optelling -1 (ongeldige waarde)

        >>> sum_col( 1, [0, 1, 6, 8, 9, 10, 11, 16, 18, 19, 60, 61, 66, 68, 69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99])
        240

        >>> sum_col( 1, [0, 1, 6, 8, 9, 10, 11, 16, 18, 19, -1, 61, 66, 68, 69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99])
        -1

    """
    totaal = 0

    for row in range(5):
        pos = row * 5 + col -1
        if oplossing[pos] == -1:
            return -1
        totaal += oplossing[pos]

    return totaal

def sum_row (row, oplossing):
    """ (int, list of int) -> int

        Return de optelsom van rij row uit oplossing (5x5 in list van 25)
        Als een element uit de rij -1 is dan wordt de optelling -1 (ongeldige waarde)

        >>> sum_row( 1, [0, 1, 6, 8, 9, 10, 11, 16, 18, 19, 60, 61, 66, 68, 69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99])
        24

        >>> sum_row( 3, [0, 1, 6, 8, 9, 10, 11, 16, 18, 19, -1, 61, 66, 68, 69, 80, 81, 86, 88, 89, 90, 91, 96, 98, 99])
        -1

    """
    totaal = 0

    for i in range(5):
        index = (row - 1) * 5 + i
        if oplossing[index] == -1:
            return -1
        totaal += oplossing[index]

    return totaal

def check_diag(oplossing):
    """ (list of int) -> bool

    controleert de diagonalen in oplossing op totaal van 264
    als de diagonalen kloppen wordt True teruggegeven anders False
    """
    # check de diagonaal NW, SE
    nw_se = 0
    for diag in [0, 6, 12, 18, 24]:
        nw_se += oplossing[diag]
    # check de diagonaal NE, SW
    ne_sw = 0
    for diag in [4, 8, 12, 16, 20]:
        ne_sw += oplossing[diag]

    if (nw_se == 264) and (ne_sw == 264):
        return True

    return False

def rotate_solution(oplossing):
    """ (list of int) -> list of int

    gebruikt oplossing en bepaalt het 180 gedraaide vierkant
    daarbij worden ook de getallen 180 graden gedraaid
    geeft een nieuwe list of int terug, past oplossing dus niet aan
    """

    # omdat de matrix als een lijst van 25 elementen is opgeslagen is roteren
    # erg makkelijk, gewoon van achter naar voren lezen en getallen omdraaien
    lengte = len(oplossing)
    rot180 = []
    for i in range(lengte):
        rot180.append(inverse[oplossing[lengte - i - 1]])
    return rot180

def check_solution (opl):
    """ (list of int) -> None

    controleer de oplossing op diagonalen en daarna ook de geroteerde variant op
    kolommen, rijen en diagonalen

    """
    if not check_diag(opl):
        return

    rot180 = rotate_solution(opl)
    for row in range(5):
        if sum_row(row, rot180) != 264:
            return False
    for col in range(5):
        if sum_col(col, rot180) != 264:
            return False

    if check_diag(rot180):
        # eindelijk een oplossing
        print_time()
        print('Goede oplossing: ')
        print_square(opl)
        print('Geroteerd: ')
        print_square(rot180)

        for char in ['d', 'w', 'y', 'b', 'e', 'a', 'v', 'g', 'x']:
            print(char + ': ' + str(opl[cw[char]]), end=', ')
        print()

        print('N52 ' + str(opl[cw['x']] + opl[cw['y']]) + '.' + str((opl[cw['a']]*opl[cw['b']]+opl[cw['w']]+93)), end=' ')
        print('E5 ' + str(59 - opl[cw['v']]) + '.' + str(opl[cw['d']] * opl[cw['e']] + opl[cw['g']]))

def print_square(square):
    """ (list of int) -> None

    print het vierkant square netjes als een vierkant van 5 x 5
    """
    for row in range(5):
        for col in range(5):
            print(str(square[row * 5 + col]).rjust(3), end='')
        print('')

def print_time():
    """ () -> None

    print de verstreken tijd sinds vorige meetpunt en pas meetpunt aan
    """
    global meetpunt, doorloop

    nwpunt = time.perf_counter()

    print('seconden            : %0.1f' % (nwpunt - meetpunt))
    doorloop += (nwpunt - meetpunt)
    meetpunt = nwpunt

def mag_square( positie, oplossing, getallen):
    """ (int, list of int, list of int) -> bool

    zoekt een oplossing voor een speciaal magisch vierkant (5x5) waarbij het magisch getal 264 is
    positie bepaald welk (nog niet gevuld) getal in oplossing gevuld moet worden. de lijst getallen
    bevat alle mogelijk waardes waaruit gekozen mag worden.
    Aanpak is om alle mogelijkheden te proberen, maar wel te stoppen met proberen als het een onmogelijke
    oplossing is (ofwel als het totaal van de huidige gevulde rij of gevulde kolom niet 264 is dan valt
    de oplossing af en geeft de functie False terug.
    Als op de laatste positie een geldige oplossing is bepaald dan wordt deze afgedrukt (en True teruggegeven)

    """
    global teller, afgewezen

    #print('positie: ' + str(positie))

    for i in range(len(getallen)):
        nw_opl = oplossing.copy()
        nw_get = getallen.copy()

        teller += 1

        pos = pos_in_oplossing[positie-1]

        nw_opl[pos-1] = nw_get[i]

        ga_verder = True

        if pos == 21:
            # controleer kolom 1 en 2 (omdat positie 22 al bepaald is)
            if (sum_col(1, nw_opl) != 264) or (sum_col(2, nw_opl) != 264):
                # we gaan niet verder
                ga_verder = False
            #else:
                # tussenresultaat
                #print('positie: ' + str(pos) + ', partieel: ' + str(nw_opl))
        elif pos == 23:
            if (sum_col(3, nw_opl) != 264):
                ga_verder = False
        elif pos == 24:
            # dit is de 1-na-laatste kolom, aangezien
            # positie 5, 5 bekend is moeten we nu kolom 4 en 5 checken voor een eindoplossing

            if (sum_col(4, nw_opl) == 264) and (sum_col(5, nw_opl) == 264):
                # we hebben een mogelijke oplossing
                check_solution(nw_opl)

            # we gaan nu nooit verder (zijn aan het eind
            ga_verder = False
        elif pos % 5 == 0:
            # controleer rijtotaal
            if sum_row( pos // 5, nw_opl) != 264:
                # we gaan niet verder
                ga_verder = False
            #else:
                # tussenresultaat
                #print('positie: ' + str(pos) + ', partieel: ' + str(nw_opl))

        # aanzet voor volgend positie
        if ga_verder:
            nw_get.pop(i)
            # nu een positie verder recursieve aanroep
            if len(nw_get) > 0:
                mag_square ( positie + 1, nw_opl, nw_get)
        else:
            afgewezen += 1



#print('oplossing : ' + str(oplossing))
#print('getallen  : ' + str(getallen))
#print('inverse   : ' + str(rotate_solution(getallen)))
#print(len(getallen))
#print(pos_in_oplossing)
#print(len(pos_in_oplossing))
# en nu gaat het beginnen
#print_square(oplossing)

# bepaal startpunt zodat de tijd voor oplossen bepaald kan worden
print('bezig met bepalen mogelijke oplossingen...')
meetpunt = time.perf_counter()
mag_square(positie, oplossing, getallen)
print_time()
print('aantal pogingen     : ' + str(teller))
print('aantal afgewezen    : ' + str(afgewezen))
print('pogingen bespaard   : ' + str(math.factorial(18) - teller))
print('totale tijd         : %0.1f' % doorloop)
print('pogingen per seconde: %0.2f' % (teller / doorloop) )


