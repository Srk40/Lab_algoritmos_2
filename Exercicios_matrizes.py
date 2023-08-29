def gbc():
    numbers = list(range(100))
    card = []

    for _ in range(25):
        index = sum(ord(c) for c in str(id(_))) % len(numbers)
        num = numbers.pop(index)
        card.append(num)

    return card

def dbc(card):
    print("Bingo Card:")
    for i in range(0, 25, 5):
        print(card[i:i+5])

bingo_card = gbc()
dbc(bingo_card)

#######################################

def sum_below_diagonal(matrix):
    total_sum = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                total_sum += matrix[i][j]
    
    return total_sum

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
print_matrix(matrix)

result = sum_below_diagonal(matrix)
print(f"\nSoma dos elementos abaixo da diagonal principal: {result}")

####################################

def withdraw_amount(amount):
    available_notes = [100, 50, 20, 10]
    withdrawal = []
    
    for note in available_notes:
        while amount >= note:
            amount -= note
            withdrawal.append(note)
    
    if amount == 0:
        return withdrawal
    else:
        return None

def display_withdrawal(withdrawal):
    if withdrawal:
        print("Notas entregues:")
        for note in withdrawal:
            print(f"R$ {note:.2f}")
    else:
        print("Não é possível sacar o valor com as notas disponíveis.")

# Exemplos de saques
withdrawal_amount_1 = 30
withdrawal_1 = withdraw_amount(withdrawal_amount_1)
print(f"Saque de R$ {withdrawal_amount_1:.2f}:")
display_withdrawal(withdrawal_1)

print()

withdrawal_amount_2 = 80
withdrawal_2 = withdraw_amount(withdrawal_amount_2)
print(f"Saque de R$ {withdrawal_amount_2:.2f}:")
display_withdrawal(withdrawal_2)

#############################################

def largest_product(matrix):
    n = len(matrix)
    max_product = 0

    for i in range(n):
        for j in range(n):
            if j + 4 < n: 
                product = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3] * matrix[i][j + 4]
                max_product = max(max_product, product)
            if i + 4 < n:  
                product = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j] * matrix[i + 4][j]
                max_product = max(max_product, product)
            if i + 4 < n and j + 4 < n:  
                product = matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3] * matrix[i + 4][j + 4]
                max_product = max(max_product, product)

    return max_product

matrix = [
    [2, 1, 1, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 2, 1],
    [1, 1, 1, 1, 2]
]

max_product = largest_product(matrix)
print(f"Maior produto de uma sequência de 5 números: {max_product}")
