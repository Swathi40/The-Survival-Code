name=input('Hello user!Enter your name:')
print(f'Hello {name},welcome to the game...!')
wanna_play=input('Do you want to play?(yes/no):').lower()
if wanna_play=='yes' or wanna_play=='y':
    weapon=input('Choose your weapon(stick/sword):').lower()
    print('Choose your direction carefully.....')
    direction=input('which direction?(left/right):').lower()
    if direction=='left':
        print('You choose the wrong direction...There is daanger!')
        print('Game Over')
    elif direction=='right':
        print('There is a Bridge in front of you')
        choice=input('how do you want to cross it?(swim/cross/boat):').lower()
        if choice=='swim' and weapon=='stick':
            print('you were eaten by an alligator....Game over!')
        elif choice=='boat' and weapon=='sword':
            print('you safely crossed the river with the stick.')
            print('Congrtulations!you survived!')
        elif choice=='cross' and weapon=='sword':
            print('You fought off the dangers and crossed the bridge.Well done!')
        else:
            print('You made an unwisenchoice. game Over!')
    else:
        print('invalid direction.Game Over!')
else:
    print('We are not playing.Goodbye!')                            
    
