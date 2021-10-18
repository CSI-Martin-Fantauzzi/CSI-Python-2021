import random

username = input("What is your name?\n")
print (f"Welcome to magic 8 ball {username}!")
answrs = ['Yes-definitely' , 'It is decidedly so.' , 'Without a doubt', 'Reply hazy, tray again.', 'Ask again later', 'Better not tell you now.', 'My sources say NO.', 'Outlook not so good.', 'Very doubtful.', 'Obviously not.', 'Not if you keep acting like that.', 'Yes, but you will regret it.']
pQ = input('Ask any question!!\n')
cANS = random.choice(answrs) 
print(f"{username} asked: {pQ}")
print(f'{cANS}')
