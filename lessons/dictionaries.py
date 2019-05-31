# ninja_belts = {'crystal': 'red', "ryu": "black"}
# #key in dict
# print("yoshi" in ninja_belts)
# print("ryu" in ninja_belts)
# # check the dict
# print(ninja_belts.keys())
# print(ninja_belts.values())

# # turn into a list

# print(list(ninja_belts.keys()))
# print(list(ninja_belts.values()))
# keys = list(ninja_belts.keys())
# vals = list(ninja_belts.values())
# print(keys)
# print(vals)

# print(vals.count('red'))


# #add to dit

# ninja_belts['yoshi'] = 'red'

# def ninja_intro(dictionary):
#     for k, v in dictionary.items():
#         print(f'i am {k} and I am a {v} belt')

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter a belt colour:')

    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n')

    if another == 'y':
        continue
    else:
        break

# ninja_intro(ninja_belts)
belt_count(ninja_belts)
