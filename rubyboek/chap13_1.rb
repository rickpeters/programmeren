# hfdst 13.1 maak je eigen classes
class Die
  def initialize
    # gewoon een keer rollen, ook al kan ik een willekeurige waarde toekennen
    roll
  end

  def roll
    @number_showing = 1 + rand(6)
  end

  def cheat value
    if value > 0 && value < 7
      @number_showing = value
    else
      puts 'invalid value'
    end
  end

  def showing
    @number_showing
  end
end

# let's make a couple of dice
dice = [Die.new, Die.new]

# ... and roll them
dice.each do |die|
  puts die.roll
end
puts

# and now with the instance variables
die = Die.new
die.roll
puts die.showing
puts die.showing
die.roll
puts die.showing
puts die.showing
puts
puts "die 1 : #{Die.new.showing || 'nil'}"
puts "die 2 : #{Die.new.cheat(3) || 'nil'}"


