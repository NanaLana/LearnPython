import random

def ask_user():
    ask = " "
    print("Введите вопрос: ")
    while True:
        ask = input()
        if ask != "Пока" :
            print(get_answer())
        else:
            break


def get_answer():
    answer = ["Ну, да", "Хорошо", "Любопытно", "Так себе"]
    return random.choice(answer)

ask_user()

