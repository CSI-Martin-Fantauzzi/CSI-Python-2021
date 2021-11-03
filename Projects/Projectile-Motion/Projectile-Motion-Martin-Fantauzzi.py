import math
from ExperimentalData import ExperimentalData

# # weapon = 'VSS' 
# # cartridge = '9x39mm'
# # ammo = 'SPP gs'
# # velocity = 310

# # building = 'Marina Torch'
# # Marina = 352

# # gravity = 9.81

def ProjectileFunction(experimentalData:ExperimentalData):
    time = math.sqrt((2 * Marina) / gravity)
    # distance = (experimentalData[velocity] * time)

#     print(f'I chose the {weapon} sniper rifle as my weapon. Its cartridge is a {cartridge} and it fires single {ammo} rounds at {velocity} meters per second. The building I chose was the {building} that reaches {Marina} meters. The bullet round took {time} seconds to reach the ground and travelled {distance} meters.')

# ProjectileFunction('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)

(7 > 6) and (3 == 5) 
not (7 > 6)
(7 > 6) or (3 == 5)
# 'velocity' : 310,
# 'building' : 'Marina Torch',
# 'Marina' : 352,
# 'gravity' : 9.81

# }
experimentalData = ExperimentalData('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)
ProjectileFunction('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)