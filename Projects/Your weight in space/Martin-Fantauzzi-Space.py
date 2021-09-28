planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
gms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print('Calculate your weight in a different planet!!')

myWeight = int(input('What is your weight in pounds?'))
myPlanet = input(f'Select a planet from the list: {planets}')

def calculateWeight(planet, mass):
    print(f'\nEarth mass in pounds is: {mass}')
        
    wkg = mass / 2.2046
    print(f"Mass in kg: {wkg}")

    n_1b = 4.45

    planet_index = planets.index(planet)
    print(f'Weight in {planets[planet_index]} is {(wkg * gms2[planet_index]) / n_1b} pounds')

calculateWeight(myPlanet, myWeight)
    




