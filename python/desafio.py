# import re

# def conta_vogais(palavra: str):
#     if not palavra:
#         raise Exception(f"string palavra não pode ser vazia ou None. valor de palavra: {palavra}")
    
#     count =  re.findall(r"[aAeEiIoOuU]", palavra)
    
#     return len(count), count
    

# def contagem(palavra: str):
#     if not palavra:
#         raise Exception(f"string palavra não pode ser vazia ou None. valor de palavra: {palavra}")
#     vogais = ["a","A","e","E","i","I","o","O","u","U"]
#     counter = [pl for pl in palavra if pl in vogais]

#     return len(counter), counter

# if __name__ == '__main__':
#     while True:
#         try:
#             palavra_ent = input("Digite uma palavra:")
#             qtd_vogais = contagem(palavra_ent)
#             if qtd_vogais[1]:
#                 vogais_formatadas = ', '.join(qtd_vogais[1])
#                 print(f"Quantidade de vogais na palavra '{palavra_ent}': {qtd_vogais}")
#                 print(f"Vogais encontradas: {vogais_formatadas}")
#             else:
#                 print(f"A palavra '{palavra_ent}' não contém vogais.")
           
#             break

#         except Exception as e:
#             print("Ocorreu um erro, tente novamente...\n")
#             continue


a = {1,34,5,57,3,4,5,7,10}
b = {0,2,34,5,69,8,10,23,65}

x = [1,34,5,57,3,4,5]
c = a - b
d = b - a
e = a & b
f = b & a


z = set(list(a)+list(b))
t = a - set(x)

input()