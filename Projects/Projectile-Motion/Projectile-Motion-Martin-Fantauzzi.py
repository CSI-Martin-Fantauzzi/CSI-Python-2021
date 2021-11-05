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

def ProjectileFunction(experimentalData:ExperimentalData):
    time = math.sqrt((2 * experimentalData.height) / experimentalData.gravity)
    # distance = (experimentalData[velocity] * time)
    distance = (experimentalData.velocity * time)

    print(f"I chose the {experimentalData.weapon} sniper rifle as my weapon. Its cartridge is a {experimentalData.cartridge} and it fires single {experimentalData.ammo} rounds at {experimentalData.velocity} meters per second. The building I chose was the {experimentalData.building} that reaches {experimentalData.height} meters. The bullet round took {time} seconds to reach the ground and travelled {distance} meters.")

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

experimentalData = ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)

myDataSet = [
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Shanghai World Financial Center', 492, 9.81),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Princess Tower', 413.4, 9.81),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Empire State Building', 381, 9.81),
    ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Bank of China Tower', 367, 9.81)
    ]

for data in myDataSet:
    print('\n-------------------------------------------------------\n')
    ProjectileFunction(data)

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile.Motion.json')

with open(myOutputFilePath, 'w') as outfile: 
    json.dump([data.__dict__ for data in myDataset], outfile) 

# ProjectileFunction('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)