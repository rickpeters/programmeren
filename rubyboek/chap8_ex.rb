# hfdst 8 arrays
# pagina 63 oefiningen

woorden = []

input = 'we moeten toch ergens beginnen'
while input != ''
  puts 'geef een woord: '
  input = gets.chomp
  if input != ''
    woorden.push input
  end
end # input loop

# nu nog sorteren en afdrukken
if woorden.length > 0
  puts 'oké, nu nog even sorteren :-)'
  puts woorden.sort.join(', ')
else
  puts 'je moet wel iets invullen, volgende keer beter'
end
