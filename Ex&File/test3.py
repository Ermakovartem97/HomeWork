planet = []
with open('objects.txt', 'r') as file:
    for line in file:
        ob = line[:-1].split(' ')
        if ob[1] == 'planet':
            planet.append(ob[0])

newPlanet = [x + '\n' for x in sorted(planet)]

with open('plan.txt', 'w') as file:
    file.writelines(newPlanet)
