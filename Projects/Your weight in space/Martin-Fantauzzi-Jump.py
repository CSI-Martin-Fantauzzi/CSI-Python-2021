planets = 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
gravity = [2.6, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88] 
print('Calculate the length of your jump on all planets!!!')

jumplength = float(input('What is the length of your jump in meters?'))
planetgravity = input(f'Select a planet from the list: {planets} ')

print(('Your jump length on Earth is: ') + str(jumplength))
planet_index = planets.index(planetgravity)
print(f'The length of your jump in {planets[planet_index]} is {((jumplength) * (gravity[planet_index]))} meters.')

