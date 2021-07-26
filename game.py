import random

while True:
    print()
    print("Привет! Хочешь поиграть?")
    game = input("Выбирай игру: [1]-Крестики нолики, [2]-Угадай число, [3]-Камень ножницы бумага: ")

    if game == '1':
        print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

        board = list(range(1, 10))


        def draw_board(board):
            print("-" * 13)
            for i in range(3):
                print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
                print("-" * 13)


        def take_input(player_token):
            valid = False
            while not valid:
                player_answer = input("Куда поставим " + player_token + "? ")
                try:
                    player_answer = int(player_answer)
                except:
                    print("Некорректный ввод. Вы уверены, что ввели число?")
                    continue
                if player_answer >= 1 and player_answer <= 9:
                    if (str(board[player_answer - 1]) not in "XO"):
                        board[player_answer - 1] = player_token
                        valid = True
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")


        def check_win(board):
            win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
            for each in win_coord:
                if board[each[0]] == board[each[1]] == board[each[2]]:
                    return board[each[0]]
            return False


        def main(board):
            counter = 0
            win = False
            while not win:
                draw_board(board)
                if counter % 2 == 0:
                    take_input("X")
                else:
                    take_input("O")
                counter += 1
                if counter > 4:
                    tmp = check_win(board)
                    if tmp:
                        print(tmp, "выиграл!")
                        win = True
                        break
                if counter == 9:
                    print("Ничья!")
                    break
            draw_board(board)


        main(board)

    if game == '3':

        print()
        print("Игра камень ножницы бумага:")
        while True:
            user_action = input("Сделайте выбор — камень, ножницы или бумага: ")
            possible_actions = ["камень", "бумага", "ножницы"]
            computer_action = random.choice(possible_actions)
            print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
            if user_action == computer_action:
                print(f"Оба пользователя выбрали {user_action}. Ничья!!")
            elif user_action == "камень":
                if computer_action == "ножницы":
                    print("Камень бьет ножницы! Вы победили!")
                else:
                    print("Бумага оборачивает камень! Вы проиграли.")
            elif user_action == "бумага":
                if computer_action == "камень":
                    print("Бумага оборачивает камень! Вы победили!")
                else:
                    print("Ножницы режут бумагу! Вы проиграли.")
            elif user_action == "ножницы":
                if computer_action == "бумага":
                    print("Ножницы режут бумагу! Вы победили!")
                else:
                    print("Камень бьет ножницы! Вы проиграли.")
            play_again = ""
            play_again = input("Сыграем еще? (д/н): ")
            if play_again.lower() != "д":
                break

    if game == '2':
        print()
        print("Игра угадай число:")


    def main():
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        result = int(input(f"Угадай результат этих чисел ({num1} * {num2}) "))
        if result == num2 * num1:
            print("Молодец")
        elif result - 5000 <= num2 * num1 <= result + 5000:
            print("Было близко")
        else:
            print("Прости, Ты слишком тупой")


    if __name__ == '__main__':
        main()
