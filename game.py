import random

def play_game():
    print('Let´s play rock, papper scissors')
    print('Choose what you want to play:\n[0] Rock\n[1] Paper\n[2] Scissors')

    wrong_element = True
    elements_game = [[0,1,2],['Rock','Papper','Scissors']]

    while wrong_element == True:   
        element = input('Input your decision: ')
        if element == '0' or element =='1' or element == '2':
            element_int = int(element)
            wrong_element = False
        else: 
            print('You chose a wrong value. Please verify your answer')

    rock_paper_scissors_random = random.randint(0,2)

    print()
    print(f'PC´s Choice: {elements_game[1][rock_paper_scissors_random]}')
    print(f'Your Choice: {elements_game[1][element_int]}')

    print('\nRESULT:')
    if element_int == rock_paper_scissors_random:
        print('The game is a tie!')
    else:
        if element_int == 0:
            if rock_paper_scissors_random == 1:
                print(f'{elements_game[1][rock_paper_scissors_random]} beats {elements_game[1][element_int]}.\nYOU LOST!')
            elif rock_paper_scissors_random == 2:
                print(f'{elements_game[1][element_int]} beats {elements_game[1][rock_paper_scissors_random]}.\nYOU WIN!')
        elif element_int == 1:
            if rock_paper_scissors_random == 0:
                print(f'{elements_game[1][element_int]} beats {elements_game[1][rock_paper_scissors_random]}.\nYOU WIN!')
            elif rock_paper_scissors_random == 2:
                print(f'{elements_game[1][rock_paper_scissors_random]} beats {elements_game[1][element_int]}.\nYOU LOST!')
        elif element_int == 2:
            if rock_paper_scissors_random == 0:
                print(f'{elements_game[1][rock_paper_scissors_random]} beats {elements_game[1][element_int]}.\nYOU LOST!')
            elif rock_paper_scissors_random == 1:
                print(f'{elements_game[1][element_int]} beats {elements_game[1][rock_paper_scissors_random]}.\nYOU WIN!')


play_game()
