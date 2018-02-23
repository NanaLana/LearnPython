def compare_strings(string_1, string_2):
    string_1 = str(string_1)
    string_2 = str(string_2)
    if string_1 == string_2:
        return ("1")
    elif len(string_1)> len(string_2):
        return ("2")
    elif string_1 != string_2 and string_2 == 'learn':
        return ("3")

string_1 = str(input("Введите первую строку: "))
string_2 = str(input("Введите вторую строку: "))
result = compare_strings(string_1, string_2)
print(result)
