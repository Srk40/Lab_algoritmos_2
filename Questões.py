
def verificar_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triângulo inválido. A soma de dois lados deve ser maior que o terceiro lado.")

    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

lado1 = 5
lado2 = 5
lado3 = 5

try:
    tipo = verificar_tipo_triangulo(lado1, lado2, lado3)
    print(f"O triângulo é {tipo}.")
except ValueError as ve:
    print(f"Erro: {ve}")


######################

def avaliar_produto():
    try:
        nota = int(input("Digite a nota do produto (de 0 a 10): "))
        assert 0 <= nota <= 10, "A nota deve estar no intervalo de 0 a 10."
        print(f"A nota {nota} foi registrada com sucesso.")
    except ValueError:
        print("Por favor, digite um número inteiro.")
    except AssertionError as ae:
        print(f"Erro: {ae}")

avaliar_produto()

#####################

class NegativeNumberError(Exception):
    pass

def calculate_square_root(numero):
    if numero < 0:
        raise NegativeNumberError("A raiz quadrada de números negativos não é real.")
    
    return numero ** 0.5

try:
    numero_input = float(input("Digite um número para calcular a raiz quadrada: "))
    resultado = calculate_square_root(numero_input)
    print(f"A raiz quadrada de {numero_input} é {resultado:.2f}.")
except ValueError:
    print("Por favor, digite um número válido.")
except NegativeNumberError as nne:
    print(f"Erro: {nne}")

###################

def find_element(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        raise IndexError("O índice fornecido é inválido para a lista.")

minha_lista = [1, 2, 3, 4, 5]

try:
    indice_input = int(input("Digite um índice para encontrar o elemento na lista: "))
    resultado = find_element(minha_lista, indice_input)
    print(f"O elemento na posição {indice_input} é {resultado}.")
except ValueError:
    print("Por favor, digite um índice válido (número inteiro).")
except IndexError as ie:
    print(f"Erro: {ie}")

########################