age_user = int(input("Введите свой возраст: "))

if 0 < age_user <= 6:
    print("Ты ходишь в садик!")
elif 7 <= age_user <=17:
    print("Ты ходишь в школу!")
elif 18 <= age_user <= 23:
    print("Ты учишься в университете!")
elif 24 <= age_user <= 55:
    print("Ты работяга!")
elif age_user <= 0:
    print("Ты ж ещё не родился!")
else:
    print("Вы на пенсии!")
