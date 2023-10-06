#first project. cool display, enter a number to choose a music genre and output a list consisting of songs (of course, chosen by me)
#
# [1] songtype1    [2] songtype2
# [3] songtype3    [4] songtype4
#
# ^ like that

MIN_INDEX = 1
MAX_INDEX = 4
import time
printn = '\n'
def mainscreen():
    
    line1 = '\n\n{:<20} {:<}'.format('[1] EDM', '[2] Metal')
    line2 = '{:<20} {:<}\n'.format('[3] Phonk', '[4] OST')
    print(line1, line2, sep='\n')
   
def input_number():
    while True:
        
        global val
        val = input('Input a number for songs with a certain genre.\nInput: ')
        
        if val.isdigit():
            val = int(val)
            if MIN_INDEX <= val <= MAX_INDEX:
                break
            else:
                print('\nEnter a number between the assigned genre numbers in the list.\n')
                time.sleep(1)
        else:
            print('\nNot a number. Please, enter a number.\n')
            time.sleep(1)
    return val

def song_output():
    xprintline = '\nHere are your songs: \n'
    if val == 1:
        print(xprintline)
        line1 = '{:<40} {:<}\n{:<40} {:<}\n'.format('Creo - Challenger', 'Creo - Aurora', 'HOME - Resonance', 'Remi Gallego - Sabotage')
        print(line1)
    elif val == 2:
        print(xprintline)
        line2 = '{:<40} {:<}\n{:<40} {:<}\n'.format('RichaadEB - VS. Susie', 'NyxTheShield - Sigma Signal', 'NyxTheShield - Alternation', 'NyxTheShield - OVERWRITE')
        print(line2)
    elif val == 3:
        print(xprintline)
        line3 = '{:<40} {:<}\n{:<40} {:<}\n'.format('Ugovhb - Serio Nem Tenta', 'Ariis - ANNIHILATE', 'YOUTHISENDING - RITMO DE TREINO', 'PLAYAMANE x Nateki - MIDNIGHT') 
        print(line3)
    elif val == 4:
        print(xprintline)
        line4 = '{:<40} {:<}\n{:<40} {:<}\n'.format('Remi Gallego - Sabotage', 'Remi Gallego - Panic Track', 'Tonspender - Slow Motion', 'Carpenter Brut - Roller Mobster')
        print(line4)
        
        
        
    
def main():
    mainscreen()
    input_number()
    song_output()

main()
    
