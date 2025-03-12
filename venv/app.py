import nltk
from nltk.sem.logic import Expression

# Inicializar el analizador de expresiones lógicas
read_expr = Expression.fromstring

# Definir constantes
yanet = read_expr('yanet')
susana = read_expr('susana')
edgar = read_expr('edgar')

# Definir los predicados con las constantes
amigos_yanet_susana = read_expr('amigos(yanet, susana)')
amigos_yanet_edgar = read_expr('no_son_amigos(yanet, edgar)')
no_amigos_edgar_susana = read_expr('tienen_la_misma_edad(edgar, susana)')
trabajan_juntos_yanet_susana = read_expr('trabajan(yanet, susana)')

# Crear un conjunto de fórmulas
formulas = [
    amigos_yanet_susana,
    amigos_yanet_edgar,
    no_amigos_edgar_susana,
    trabajan_juntos_yanet_susana
]

# Imprimir las fórmulas para verificar
for formula in formulas:
    print(formula)
