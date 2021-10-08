import random
print("Hello I am RPS!! Let's play Rock, Paper,Scissors!! ")
RPS = ['Rock', 'Paper', 'Scissors']

pChoice = input('Choose between Rock, Paper, Scissors!!\n')
cChoice = random.choice(RPS)

print(f"Computer selected: {cChoice}")
print(f'Player selected: {pChoice}')

if(pChoice == cChoice):
    print('You tied with me >:|')

elif(pChoice == 'Rock' and cChoice == 'Scissors'):
    print('You won >:(')

elif(pChoice == 'Scissors' and cChoice == 'Paper'):
    print('You won >:(')

elif(pChoice == 'Paper' and cChoice == 'Rock'):
    print('You won >:(')

elif(pChoice == 'Rock' and cChoice == 'Paper'):
    print('You lost >:)')

elif(pChoice == 'Scissors' and cChoice == 'Rock'):
    print('You lost >:)')

elif(pChoice == 'Paper' and cChoice == 'Scissors'):
    print('You lost >:)')

else:
    print('Looks like you did something wrong :(')

