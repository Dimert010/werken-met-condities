#SETUP
yes_no = ['yes', 'no']
directions = ['left', 'right', 'forward', 'backwards']

#intro
print('you wake up in a forest.')
print('you dont remember where you came from and dont no the way out the forest.')
print('find a way out of the forest.')

#start 
answer = ""
while answer not in yes_no:
    answer = input ('do you want to walk around? \nyes/no\n')
    if answer == 'yes':
        print('you start walking around.')
    elif answer == 'no':
        print('you starving to dead.')
        quit()

#BEGINNING oF THE GAME
answer = ""
while answer not in directions:
    print('you found a path and walk on it,')
    print('you are in front of a bifuraction')
    print('you can left or right.')
    answer = input('which directions do you want to go? \nleft/ right\n')
    if answer == 'left':
        print('you got eaten alive by a pack of wolves. \nDeaD\n')
        quit()
    elif answer == 'right':
        print('you walk further on the path')

#second part of the game
answer = ""
while answer not in yes_no:
    print('you walk on the path you found.')
    print('in the distance you saw an house.')
    print('you walk towards the house')
    answer = input('do you want to go inside the house? \nyes/no\n')
    if answer == 'yes':
        print('you going inside the house.')
    elif answer == 'no':
        print('you walk away from the house and got killed by some bandits.') 
        quit()
    
#third part of the game
answer = ""
while answer not in yes_no:
    print('you found a chest inside.')
    answer =  input('to you want to open the chest? \nyes/no\n')
    if answer == 'yes':
        print('you look inside the chest and found a sword.')
    elif answer == 'no':
        print('walk away from the chest, apperrently the chest was cursed and it killed you.\ndead\n')
        quit()
    answer = input('to you want pick up the sword?\nyes/no\n')
    if answer == 'yes':
        print('you  have pickup the sword and left the house.')
    elif answer == 'no':
        print('walk away from the chest, apperrently the chest was cursed and it killed you.\ndead\n')
        quit()

#fourth part of the game
answer = ""
while answer not in yes_no:
    print('you are outside the house.')
    print('you got jump by bandits.')
    answer = input('do you want to fight back.\nyes/no\n')
    if answer == 'yes':
        print('you fought back and won.')
    elif answer == 'no':
        print('you got killed.\nDeaD\n')

#five part of the game 
answer = ""
while answer not in directions:
    print('you walked away from the battle and found a crossing')
    answer = input('do you want to go straigth, left or right?\nstraight/left/right\n')
    if answer == 'straight':
        print('you found yourself at a edge of a ravine. the edge of the ravine is broken and you fall to your dead.\ndead\n')
    elif answer == 'left':
        print('you found some plants. they where poisonous.\nDeaD\n')
        quit()
    elif answer == 'right':
        print('you walk further on path and got thirsty.')

#part six of the game 
answer = ""
while answer not in yes_no:
    print('when you walk on the path you found a lake.')
    answer = input('do you want to drink some water out of the lake? \nyes/no\n')
    if answer == 'yes':
        print('you drink some water from the lake.')
    elif answer == 'no':
        print('you are drying out and you are dying.\ndead\n')

#final part of the game
answer = ""
while answer not in directions:
    print('you at the end of the forest.')
    answer = input('do you want to go straight to the end of the forest or do you want to go back to the forest? \nstraight/backwards\n')
    if answer == 'straight':
        print('you are leaving the forest and found  your found a house.')
    elif answer == 'backwards':
        print('you go back in to the forest.\ngameover\n')
        quit()
    print('yous stand in front of the house.')
    answer = input('do you want to go inside the house?\nyes/no\n')
    if answer == 'yes':
        print('you go inside the house.')
    elif answer == 'no':
        print('you are ignoring the house and go explore the rest of the world.\npart 2?\n')
        quit()
    answer = input('you are inside the house. do you want to explore the house?\nyes/no\n')
    if answer == 'yes':
        print('you are exploring the house and found out that it is youre house.')
    elif answer == 'no':
        print('you walk out of the house and go explore the world.\npart 2?\n')
        quit()
    print('you found out that is your house.')
    answer = input('do you want to relax? \nyes/no\n')
    if answer == 'yes':
        print('you are relaxing. \nend of game\n')
        quit()
    elif answer == 'no':
        print('you left the house and exlporing the world. \ngame over\n')
        quit()
