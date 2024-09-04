## Question 5

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Digite um Texto: ")
print("Texto invertido:", inverter_string(string))
