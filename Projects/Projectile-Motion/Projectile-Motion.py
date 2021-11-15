import math
from ExperimentalData import ExperimentalData

from pathlib import Path
import json
import os
# # experimentalData.weapon = 'VSS' 
# # experimentalData.cartridge = '9x39mm'
# # experimentalData.ammo = 'SPP gs'
# # experimentalData.velocity = 310

# # experimentalData.building = 'Marina Torch'
# # experimentalData.height = 352

# # experimentalData.gravity = 9.81

# convert your variables into parameters

def ProjectileFunction(experimentalData:ExperimentalData):

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    gravity = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]
    time = math.sqrt((2 * experimentalData.height) / experimentalData.gravity)
    # distance = (experimentalData[velocity] * time)
    distance = (experimentalData.velocity * time)
    

    print(f"I chose the {experimentalData.weapon} sniper rifle as my weapon. Its cartridge is a {experimentalData.cartridge} and it fires single {experimentalData.ammo} rounds at {experimentalData.velocity} meters per second. The building I chose was the {experimentalData.building} that reaches {experimentalData.height} meters. The bullet round took {time} seconds to reach the ground and travelled {distance} meters. This was on planet {experimentalData.planets}.")

# Convert parameters (variables) into a JSON 

# experimentalData = {

# 'weapon' : 'VSS', 
# 'cartridge' : '9x39mm',
# 'ammo' : 'SPP gs',
# 'velocity' : 310,
# 'building' : 'Marina Torch',
# 'height' : 352,
# 'gravity' : 9.81

# }

# experimentalData = ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)

# Create a Python class

myDataSet = [
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81, 'Earth'),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Shanghai World Financial Center', 492, 3.7, 'Mercury'),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Princess Tower', 413.4, 8.87, 'Venus'),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Empire State Building', 381, 3.711, 'Mars'),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Bank of China Tower', 367, 24.79, 'Jupiter')
]

# Write a For-Loop
for data in myDataSet:
    print('\n-------------------------------------------------------\n')
    ProjectileFunction(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile.Motion.json')

print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile: 
    json.dump([data.__dict__ for data in myDataSet], outfile) 

# Deserialization
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    ExperimentalData(**e)


# ProjectileFunction(experimentalData)