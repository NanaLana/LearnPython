# user_name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# i=0
# n = len(user_name)
# while (i <n):
#     elif user_name[i] == "Валера":
#         print(user_name.pop(i) + " нашёлся")
#         break
#     i = i+1
#

def find_person(name):
    user_name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    i = 0
    n = len(user_name)
    while (i < n):
        if (user_name[i] == name):
            result = user_name.pop(i)
            print(result + " нашёлся")
            break
        i = i +1

name = (input("Введите имя: "))
find_person(name)



