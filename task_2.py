# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.

from random import randint

# выбор режима игры и уровня сложности бота
def select_mod(first_player: str) ->str: 

    n = int(input(f'{first_player} if you want to play alone -> press 1, if you play with your freand -> press 2: '))
    if n == 2:
        second_player = input("write your friend's name: ")
        print(f'Hello, {second_player}')    
    else: 
        bot_mod = int(input(f'{first_player} select the bot level, if low -> press 1, if high -> press 2: '))
        if bot_mod == 1:
            second_player = 'low_bot'
        else: second_player = 'high_bot'
    return second_player


# жеребьевка первого хода
def lottery(first_player: str, second_player: str) ->int:
    print("to find out which of you will walk first, let's draw lots")
    number_p_f = int(input(f'{first_player} Enter any number: ' ))

    if second_player == 'low_bot' or second_player == 'high_bot':
        number_p_s = randint(0, 100)
        print(f'The bot entered {number_p_s}')
    else:
        number_p_s = int(input(f'{second_player} Enter any number: ' ))

    lucky_num_p_f = randint(0, 100)
    lucky_num_p_s = randint(0, 100)

    if abs(number_p_f - lucky_num_p_f) > abs(number_p_s - lucky_num_p_s):
        print(f'The winner of the draw {first_player}, сongratulate')  
        n = 1      
    else: 
        print(f'The winner of the draw {second_player}, сongratulate')
        n = 2
    return n


# логика легкого бота
def low_bot_mod(total_candies: int, taken_candies_max: int) ->int:
    if total_candies > taken_candies_max:
        n = randint(1, taken_candies_max)
    else:
         n = total_candies
    return n


# логика тяжелого бота
def high_bot_mod(total_candies: int, taken_candies_max: int) ->int:
    if total_candies > taken_candies_max:
        n = total_candies % (taken_candies_max + 1)
        if n == 0:
            n = taken_candies_max
    else:
         n = total_candies
    return n


# игра с конфетами
def game(total_candies: int, first_player: str, second_player: str, winner_lottery: int, taken_candies_max: int) ->str:
    if winner_lottery == 2:
        temp = first_player
        first_player = second_player
        second_player = temp

    winner = ''
    while total_candies > 0:
        winner = first_player
        if first_player == 'low_bot':
           taken_candies = low_bot_mod(total_candies, taken_candies_max)
           print(f'The bot take candies the: {taken_candies}')
        elif first_player == 'high_bot':
            taken_candies = high_bot_mod(total_candies, taken_candies_max)
            print(f'The bot take candies the: {taken_candies}')
        else:
            taken_candies = int(input(f"{first_player} Enter number of candies. It should be in range [1...28]: "))

        total_candies -= taken_candies
        print(f'There are some sweets left in the basket: {total_candies}')

        if total_candies > 0:
            winner = second_player
            if second_player == 'low_bot':
                taken_candies = low_bot_mod(total_candies, taken_candies_max)
                print(f'The bot take candies the: {taken_candies}')
            elif second_player == 'high_bot':
                taken_candies = high_bot_mod(total_candies, taken_candies_max)
                print(f'The bot take candies the: {taken_candies}')
            else:
                taken_candies = int(input(f"{second_player} Enter number of candies. It should be in range [1...28]: "))
            
        total_candies -= taken_candies
        print(f'There are some sweets left in the basket: {total_candies}')

    print(f'{winner} win, сongratulate')    


total_candies = 220
taken_candies_max = 28

first_player = input('Hello, what is yoir name: ')
second_player = select_mod(first_player)
winner_lottery = lottery(first_player,  second_player)
# winner_game = game(total_candies, first_player, second_player, winner_lottery, taken_candies_max)

# if winner_game == first_player:
#     print(f'{first_player} win, сongratulate')
# else:
#     print(f'{second_player} win, сongratulate')

game(total_candies, first_player, second_player, winner_lottery, taken_candies_max)





