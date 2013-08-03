# hfdst 10, recursie, bereken continent grootte
$DEBUG = false

M = 'l'  # land
o = 'w'  # water

world = [[o,o,o,o,o,o,o,o,o,o,o],
         [o,o,o,o,M,M,o,o,o,o],
         [o,o,o,o,o,o,o,o,M,M,o],
         [o,o,o,M,o,o,o,o,o,M,o],
         [o,o,o,o,o,M,M,o,o,o,o],
         [o,o,o,o,M,M,M,M,o,o,o],
         [M,M,M,M,M,M,M,o,o,M,M],
         [o,o,o,M,M,o,M,M,o,o,o],
         [o,o,o,o,o,o,M,M,o,o,o],
         [o,M,o,o,o,M,o,o,o,o,o],
         [o,o,o,o,o,o,o,o,o,o,o]]

def continent_size world, x, y
  # de extra opgave is om te valideren of x en y wel valide zijn
  # niet zozeer vanuit niet gedefinieerde cellen, want die krijgen
  # de waarde nil en dat gaat goed.
  # maar ruby kent een bijzondere eigenschap tav negatieve array indexen
  # een negatieve waarde telt vanaf de upper limit van een array
  # dus world[0][-1] is de laatste cel van het 1e array element
  # dit is van belang als vanuit een cel de buurmannen worden bekeken
  # want dan kunnen de indexen negatief worden
  # effect is dat landen die aan de rechter-rand liggen meegeteld worden
  # als je vanuit links gaat uitbreiden [M,o,M,M] zou één land opleveren
  # dus de check moet gedaan worden op een waarde tussen de grenzen
  # tweede uitdaging is het bepalen van de grenzen zelf. Dit moet voor de hoofd-array
  # en vervolgens daarbinnen voor de sub-array
  if y < 0 || y > world.size - 1
    if $DEBUG then (puts 'tile ' + x.to_s + ', ' + y.to_s + ': over de rand, aaaaah!') end
    return 0
  end
  if x < 0 || x > world[y].size - 1
    if $DEBUG then (puts 'tile ' + x.to_s + ', ' + y.to_s + ': over de rand, aaaaah!') end
    return 0
  end

  if world[y][x] != 'l'
    # het is of water, of we hebben deze al geteld
    # in ieder geval willen we deze niet opnieuw tellen
    if $DEBUG then (puts 'tile ' + x.to_s + ', ' + y.to_s) end
    return 0
  end

  # eerst deze maar eens tellen
  size = 1
  world[y][x] = 'c' # counted land
  $DEBUG  ? (puts 'tile ' + x.to_s + ', ' + y.to_s + ' land in zicht!') : nil


  # dan gaan we de omliggende tegels tellen
  # en via recursie gaat het dan vanaf daar gewoon weer verder
  size = size + continent_size(world, x-1, y-1)
  size = size + continent_size(world, x  , y-1)
  size = size + continent_size(world, x+1, y-1)
  size = size + continent_size(world, x-1, y  )
  size = size + continent_size(world, x  , y  )
  size = size + continent_size(world, x+1, y  )
  size = size + continent_size(world, x-1, y+1)
  size = size + continent_size(world, x  , y+1)
  size = size + continent_size(world, x+1, y+1)

  # en we geven het gewenste resultaat terug
  size
end


#if world[12][12] == nil
#  puts 'ja'
#else
#  puts 'nee'
#end

if $DEBUG
  puts 'grootte wereld: ' + world.size.to_s
  puts 'grootte wereld[1]: ' + world[1].size.to_s
  puts 'grootte wereld[2]: ' + world[2].size.to_s
end

def print_world(world)
# print world
  y = 0
  while y < world.size
    puts world[y].join ', '
    y = y + 1
  end
end

print_world(world)
puts
puts 'resultaat : ' + continent_size(world, 5, 5).to_s
puts
print_world(world)
