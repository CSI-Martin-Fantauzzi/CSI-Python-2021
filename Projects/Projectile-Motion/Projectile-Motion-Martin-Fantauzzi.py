weapon = 'VSS' 
cartridge = '9x39mm'
ammo = 'Full-Auto'
velocity = 900

building = 'Marina Torch'
Marina = 352

gravity = 9.81

import math
time = math.sqrt((2 * Marina) / gravity)
distance = velocity * time

print(f'I chose the {weapon} sniper rifle as my weapon. Its cartridge is a {cartridge} and it fires {ammo} rounds at {velocity} RPM. The building I chose was the {building} that reaches {Marina} meters. The bullet round took {time} seconds to reach the ground and travelled {distance} meters.')

