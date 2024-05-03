# import re

# # String de exemplo
# texto = 'RSD010001'

# # Padrão de regex para capturar os últimos quatro dígitos numéricos após 'RSD' seguido de dois dígitos
# # padrao = r'(?:RSD\d{2})(\d{4}$)'
# padrao = r'(?:.)(\d{4}$)'

# # Encontrar a correspondência usando regex
# correspondencia = re.search(padrao, texto)

# # Verificar se a correspondência foi encontrada
# if correspondencia:
#     # Obter os últimos quatro dígitos numéricos como grupo capturador
#     ultimos_quatro_digitos = correspondencia.group(1)
#     print(ultimos_quatro_digitos)  # Saída: '0001'
# else:
#     print('Nenhum padrão encontrado')


# import ast

# # Variável com o valor 'False' como string
# valor_string = 'True'

# # Convertendo para bool usando ast.literal_eval()
# valor_booleano = ast.literal_eval(valor_string)
# print(valor_booleano)  # Saída: False



def teste(list_str: list):
    result = []
    import re
    for st in list_str:
        search = re.findall(r'\d+', str(st))
        if '' in search:
            search.remove('')
        if search:

            
            print("A expressão regular foi encontrada na string.")
        else:
            print("A expressão regular não foi encontrada na string.")
           
    return result

teste_v = teste([{""}, {" "},  {" 321312"},  {" asd 321312"}, {"13412421"}, {"asd 321312"}, {"dasda312312"}, {"dasd"}, {"4343"}])

