# hfdst 10, recap

def ask_recursief (question)
  puts question
  reply = gets.chomp.downcase

  if reply == 'ja'
    true
  elsif reply == 'nee'
    false
  else
    puts 'antwoord alsjeblieft met "ja" of "nee"'
    ask_recursief question # magic line
  end
end

ask_recursief 'hou je van tacos?'
ask_recursief 'hou je van burritos?'
wets_bed = ask_recursief 'plas je wel eens in bed?'

puts
puts 'Evaluatie:'
puts 'Bedankt voor de medewerking...'
puts
puts wets_bed
