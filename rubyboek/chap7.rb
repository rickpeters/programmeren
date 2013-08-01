# pagina 43
puts 'ant'          < 'Zoo'
puts 'ant'.downcase < 'Zoo'.downcase

# pagina 44
puts 'Hallo, wat is je naam?'
naam = gets.chomp
puts 'Hallo, ' + naam + '.'

if naam == 'Rick' || naam == 'Leikur'
  puts 'Wat een mooie naam!'
elsif naam == 'Hermien'
  puts 'jeetje, dat is ook een leuke naam!'
else
  puts 'Oh jee, jouw ouders hebben hier ook niet echt over nagedacht :-)'
end  # branching sample

input = ''

while input != 'doei'
  puts input
  input = gets.chomp
end

puts 'tot binnenkort!'

puts self