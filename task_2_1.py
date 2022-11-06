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

CNT_CANDY = 2021
CNT_PLAYERS = 2
MAX_CANDY_STEP = 28
MIN_CANDY_STEP = 1

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2',
    3: 'Low_bot',
    4: 'High_bot'
}

def get_first_move_player() -> int:
    """
    Случайный выбор игрока, который будет ходить первым
    :return: номер игрока (1/2)
    """
    return randint(1, CNT_PLAYERS)

def valid_cnt_candy(cnt: int) -> bool:
    """
    Проверка количества выбранных пользователем конфет
    :param cnt: количество конфет
    :return: True/False
    """

    if MIN_CANDY_STEP <= cnt <= MAX_CANDY_STEP:
        return True
    else:
        return False

def valid_type_value_cnt_candy(cnt: str) -> bool:
    """
    Введенное пользователем значение - целое число?

    :param cnt: введенное пользователем значение
    :return: True / False
    """

    if cnt.isdigit():
        return True
    else:
        return False

def valid_value_cnt_candy(cnt: int, full_cnt: int, players_candies: dict) -> bool:
    """
    Не превышает введенное пользователем значение количество
    оставшихся конфет
    :param players_candies: количество конфет на руках у игроков
    :param full_cnt: всего конфет
    :param cnt: желаемое пользователем количество конфет
    :return: True/False
    """

    if (full_cnt - (players_candies[1] + players_candies[2])) < cnt:
        return False
    else:
        return True

def get_remainder(players_candies: dict, full_cnt: int) -> int:
    """
    Подсчет количества оставшихся конфет
    :param players_candies: количество конфет на руках у игроков
    :param full_cnt: всего конфет
    :return: количество оставшихся конфет
    """

    return full_cnt - (players_candies[1] + players_candies[2])

def start_game_human_human():
    """
    Игра в режиме человек с человеком
    :return: None
    """
    cnt_candy_players: dict = {
        1: 0,
        2: 0
    }

    id_player: int = get_first_move_player()

    while (cnt_candy_players[1] + cnt_candy_players[2]) < CNT_CANDY:
        current_cnt_candy = input(f"{PLAYERS_NAMES[id_player]}, Ваш ход: ")

        if not valid_type_value_cnt_candy(current_cnt_candy) or not valid_cnt_candy(int(current_cnt_candy)):
            print(f"Допустимое число конфет [{MIN_CANDY_STEP} , {MAX_CANDY_STEP}]")
            continue

        if not valid_value_cnt_candy(int(current_cnt_candy), CNT_CANDY, cnt_candy_players):
            print(f"{PLAYERS_NAMES[id_player]}, Вы не можете взять больше конфет, чем осталось")
            continue

        cnt_candy_players[id_player] += int(current_cnt_candy)

        print(f"Осталось конфет: {get_remainder(cnt_candy_players, CNT_CANDY)}")

        id_player = 1 if id_player == 2 else 2

    print(f"Победу одержал {PLAYERS_NAMES[1 if id_player == 2 else 2]}")

start_game_human_human()