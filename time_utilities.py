#to convert hours.minutes (float) in hours.hours
def ore_minuti_in_ore(ore_minuti):
    ore=int(ore_minuti)
    minuti= (ore_minuti - ore)/0.60
    tempo_in_ore= ore + minuti
    return tempo_in_ore
