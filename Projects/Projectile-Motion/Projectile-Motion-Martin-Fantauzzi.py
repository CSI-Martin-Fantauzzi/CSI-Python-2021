import math

# weapon = 'VSS' 
# cartridge = '9x39mm'
# ammo = 'SPP gs'
# velocity = 310

# building = 'Marina Torch'
# Marina = 352

# gravity = 9.81

def ProjectileFunction(weapon:str, cartridge:str, ammo:str, velocity:int, building:str, Marina:int, gravity:int):
    time = math.sqrt((2 * Marina) / gravity)
    distance = (velocity * time)

    print(f'I chose the {weapon} sniper rifle as my weapon. Its cartridge is a {cartridge} and it fires single {ammo} rounds at {velocity} meters per second. The building I chose was the {building} that reaches {Marina} meters. The bullet round took {time} seconds to reach the ground and travelled {distance} meters.')

ProjectileFunction('VSS','9x39mm', 'SPP gs', 310, 'Marina Torch', 352, 9.81)