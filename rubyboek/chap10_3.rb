# hfdst 10 sorteren
# recursieve wijze sorteren

def sort some_array # this wraps recursive sort
  recursive_sort some_array, []
end

def recursive_sort unsorted_array, sorted_array
  # en hier komt mijn fantastische code
  # eerst de eindconditie van de recursie, anders houdt het nooit op
  if unsorted_array.size == 0
    return sorted_array
  end

  # de array om de unsorted in op te bouwen
  new_unsorted_array = []
  kleinste_woord = unsorted_array[0]
  # loop langs de ongesorteerde array
  i = 1
  while i < unsorted_array.size
    # kijk of huidige woord kleiner is dan kleinste_woord
    if kleinste_woord.downcase < unsorted_array[i].downcase
      # we zitten nog goed, huidige woord kan naar new_unsorted_array
      new_unsorted_array.push unsorted_array[i]
    else
      # kleinste woord kan naar new_ubsorted_array, en we hebben een nieuw kleinste_woord
      new_unsorted_array.push kleinste_woord
      kleinste_woord = unsorted_array[i]
    end
    i = i + 1
  end

  # we hebben nu het kleinste woord bepaald, dit kan naar sorted_array
  sorted_array.push kleinste_woord

  # en nu gaan we recursief
  recursive_sort new_unsorted_array, sorted_array

  return sorted_array
end

puts sort ['mies', 'noot', 'aap', 'wim', 'jet', 'klaas']
