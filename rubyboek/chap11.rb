# hfdst 11, reading and writing
# pag. 98
require 'yaml'

def yaml_save(object, filename)
  File.open filename, 'w' do |f|
    f.write(object.to_yaml)
  end
end

def yaml_load(filename)
  yaml_string = File.read filename

  YAML::load yaml_string
end

test_array = ['oooh, quiche is lekker',
              'mutanten niet welkom',
              'kameleon-achtigen, nee dankje',
              'Chameleonic Life-Forms, No Thanks',
              '42',
              42,
              'true',
              true,
              [4, 3, 18, Math::PI, 'Math::PI']
             ]

test_array = test_array + [['aap', 'noot', 'mies']]

filename = 'RimmerTShirts.txt'

# bewaren
yaml_save test_array, filename

# en weer lezen
read_array = yaml_load filename

puts(read_array  == test_array )