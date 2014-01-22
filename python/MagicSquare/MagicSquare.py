"""
een programma om voor de geocache twee zes vier een magisch vierkant
te bepalen waarvoor geldt dat het magisch getal 264 is, het 5 x 5 velden bevat.
De te gebruiken getallen zijn alle 2-cijferige combinaties van de getallen 0, 1, 6, 8 en 9 (met voorloopnul)
Dus 25 getallen
Verder kan het vierkant 180 graden gedraaid worden waarbij de getallen omgekeerd worden gelezen (16 wordt 91)
en is het dan nog steeds een magisch vierkant met het magisch getal 264

pseudocode:

def functie sumcol (col, oplossing) integer

def functie sumrow (row, oplossing) integer

def functie magsquare( positie, oplossing, getallen) bool
for i = 0 to len(getallen) - 1
  nw_opl = kopieer oplossing
  nw_get = kopieer getallen
  nw_opl[pos_in_oplossing[positie]] = getallen[i]
  if pos_in_oplossing[positie] % 5 = 0
   // controleer rijtotaal
    if sumrow( pos_in_oplossing[positie] // 5 + 1) != 264
      // hier hoeven we niet verder te gaan
      return False
  if pos_in_oplossing between 21 and 24
    // controleer kolomtotaal
    if sumcol(pos_in_oplossing[positie] - 20) != 264
      // hier hoeven we niet verder te gaan
      return False
  if pos_in_oplossing[positie] == 25
    if sumcol(5, nw_opl) != 264
      // geen oplossing
      return False
    else
      // oplossing
      print nw_opl
      return True


  // aanzet voor volgend positie
  verwijder nw_get[i]
  // nu een positie verder recursieve aanroep
  if not magsquare ( positie + 1, nw_opl, nw_get)
    // huidige richting niet juist
    return False


// hoofdprogramma, initialisatie
positie = 1
oplossing = {uitgangspositie}
getallen = {de 17 beschikbare getallen}
pos_in_oplossing = {positie van n-de getal in de oplossing omdat bepaalde posities al bezet zijn)
// aanroep naar het echte werk
magsquare( positie, oplossing, getallen )

"""

positie = 1
oplossing = {89, -1, -1, -1, -1,
             -1, 61, -1, 86, -1,
             16, -1,  0, -1, -1,
             -1, -1, 66, 18, -1,
             -1, 10, -1, -1, 96}

getallen = {1, 6, 8, 9, 11, ...}
pos_in_oplossing = {2, 3, 4, 5, 6, 8, 10, 12, 14, 15, 16, 17, 20, 21, 23, 24}

print(oplossing)
print(getallen)
print(pos_in_oplossing)
print(len(pos_in_oplossing))

