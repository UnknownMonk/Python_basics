import random

wins = 0
losses = 0
ties = 0

cmds = ['r', 'p', 's']

while True:
    cmd = input('please input r/p/s:')
print(f'{wins} {losses} {ties}')
oppent_cmd = cmds[random.randrange(0, 3)]
if cmd == 'r':
    if oppent_cmd == 'r':
        print('you tie')
        elif
    break
    else:
        print('I didnt under stand')

        print('Thank you for playing')
