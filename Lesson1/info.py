# def get_summ(one, two, delimeter=' '):
#     x = str(one) + str(delimeter) + str(two)
#     return x.upper()
#
# print(get_summ("привет", "олег", ","))
#
#

def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answers[question]

user_string=input("Что-нибудь ")
print(get_answer(user_string.lower()))
