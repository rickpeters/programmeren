# pagina 43
puts 'ant'          < 'Zoo'
puts 'ant'.downcase < 'Zoo'.downcase

# pagina 44
puts 'Hallo, wat is je naam?'
naam = gets.chomp
puts 'Hallo, ' + naam + '.'

if naam == 'Rick'
  puts 'Wat een mooie naam!'
else
  puts 'Oh jee, jouw ouders hebben hier ook niet echt over nagedacht :-)'
end

input = ''

while input != 'doei'
  puts input
  input = gets.chomp
end

puts 'tot binnenkort!'