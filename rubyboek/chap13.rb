# hfdst 13
# creating new classes, changing existing ones
class Integer
  def to_eng
    if self == 5
      english = 'five'
    else
      english ='forty-two'
    end

    english
  end

  def factorial
    if self < 0
      return 'je kunt geen faculteit bepalen van een negatief selfmer'
    end

    if self <= 1
      1
    else
      self * (self-1).factorial
    end
  end

end


puts 3.factorial
puts 30.factorial
puts

puts 5.to_eng
puts 42.to_eng
puts 6.to_eng