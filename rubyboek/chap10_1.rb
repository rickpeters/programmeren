# hfdst 10 recursie
def factorial num
  if num < 0
    return 'je kunt geen faculteit bepalen van een negatief nummer'
  end

  if num <= 1
    1
  else
    num * factorial(num-1)
  end
end

puts factorial(3)
puts factorial(30)