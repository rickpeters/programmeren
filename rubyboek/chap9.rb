# hfdst 9 methods
def say_moo number_of_moos
  puts 'moooooooooo...'*number_of_moos
  'yellow submarine'
end

return_val = say_moo 3
puts 'oink oink'
puts 'say_moo returned:'
puts return_val


def ask question
  while (true)
    puts question
    reply = gets.chomp.downcase
    if (reply == 'ja' or reply == 'nee')
      if reply == 'ja'
        return true
      else
        return false
      end
    else
      puts 'antwoord alsjeblieft met "ja" of "nee"'
    end
  end

  answer # dit is de waarde die we terug geven
end

ask 'hou je van tacos?'
ask 'hou je van burritos?'
wets_bed = ask 'plas je wel eens in bed?'

puts
puts 'Evaluatie:'
puts 'Bedankt voor de medewerking...'
puts
puts wets_bed
