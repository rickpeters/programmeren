# hfdst 13.1 maak je eigen classes
class Die
  def roll
    @number_showing = 1 + rand(6)
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
puts "die : #{Die.new.showing || 'nil'}"
puts (Die.new.showing || 'nil')


