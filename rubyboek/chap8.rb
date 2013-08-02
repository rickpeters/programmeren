# chapter 8 arrays and iterations
names = []
names[0] = 'Rick'
names[1] = 'Hermien'
names[2] = 'Myrthe'
names[3] = 'Sander'

puts names
puts

index = 0
while index < 4
  puts names[index]
  index += 1
end

puts names[4]

names.each do |name|
  puts name + ' is een hele leuke naam!'
  puts 'vind je ook niet?'
end

puts names.length

3.times do
  puts 'hiep hiep HOERA!'
end

foods = ['artisjok', 'broccoli', 'caramel']

puts foods
puts
puts foods.to_s
puts
puts foods.join(', ')
puts
puts foods.join(' :) ') + ' 8)'

animals = [ ['paard', 'ezel'], ['konijn', 'hamster', 'cavia'], ['herder', 'ijsco']]
puts animals
puts animals.to_s
puts animals.join(', ')
puts
puts animals.pop
puts
puts animals.last

