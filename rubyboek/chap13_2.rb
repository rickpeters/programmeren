# hdst 13: Dragon class
class Dragon

  def initialize name
    @name               = name
    @asleep             = false
    @stuff_in_belly     = 10 # he's full
    @stuff_in_intestine = 0 # he doesn't need to go

    puts @name + ' is geboren'
  end

  def feed
    puts 'Hmmm lekker... zegt ' + @name +'.'
    @stuff_in_belly = 10
    passage_of_time
  end

  def walk
    puts 'Lekker even wandelen... zegt ' + @name + '.'
    @stuff_in_intestine = 0
    passage_of_time
  end

  def put_to_bed
    puts @name + ' zegt welterusten, ik lig lekker in bed.'
    @asleep = true
    3.times do
      if @asleep
        passage_of_time
      end
      if @asleep
        puts @name + ' snurkt en vult de kamer met rook.'
      end
    end
    if @asleep
      @asleep = false
      puts @name + ' wordt langzaam wakker.'
    end
  end

  def toss
    puts 'je gooit ' + @name + ' lekker door de lucht.'
    puts 'hij moet lachen en verschroeit je wenkbrauwen.'
    passage_of_time
  end

  def rock
    puts 'je wiegt ' + @name + ' zachtjes'
    @asleep = true
    puts 'hij dommelt kort weg...'
    passage_of_time
    if @asleep
      @asleep = false
      puts '...maar wordt wakker als je stopt.'
    end
  end

  private
  # dit betekent dat de methodes die hier staan intern zijn voor het object
  # deze kun je dus van buiten niet gebruiken. Je kunt de draak voeren, maar niet
  # vragen of hij honger heeft

  def hungry?
    # method naam kan eindigen met "?"
    # dit is gebruikelijk om te doen als de methode
    # true of false terug geeft
    @stuff_in_belly <= 2
  end

  def poopy?
    @stuff_in_intestine >= 8
  end

  def passage_of_time
    if @stuff_in_belly > 0
      # verplaats voedsel van de buik naar de darmen
      @stuff_in_belly     = @stuff_in_belly     - 1
      @stuff_in_intestine = @stuff_in_intestine + 1
    else # onze draak verhongert
      if @asleep
        @asleep = false
        puts 'Hij wordt plotseling wakker!'
      end
      puts @name + ' verhongert! Uit pure wanhoop eet hij JOU op!'
      exit # hiermee stopt het programma
    end

    if @stuff_in_intestine >= 10
      @stuff_in_intestine = 0
      puts 'O jee...! ' + @name + ' heeft een ongelukje gehad...'
    end

    if hungry?
      if @asleep
        @asleep = false
        puts 'hij wordt plotseling wakker!'
      end
      puts 'de buik van ' + @name + ' rommelt...'
    end

    if poopy?
      if @asleep
        @asleep = false
        puts 'hij wordt plotseling wakker!'
      end
      puts @name + ' gaat netjes op het potje...'
    end
  end

end

pet = Dragon.new 'Finn'
pet.feed
pet.toss
pet.walk
pet.put_to_bed
pet.rock
pet.put_to_bed
pet.put_to_bed
pet.put_to_bed
pet.put_to_bed