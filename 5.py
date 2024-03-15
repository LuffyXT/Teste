def inverter_string(string):
    inverted_string = ''
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

string = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(string))