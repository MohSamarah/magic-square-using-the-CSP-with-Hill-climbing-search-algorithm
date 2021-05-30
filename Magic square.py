# Mohammed Alsamarah 128384
import random
import time

generate_number = list(range(1, 17))
magic_square = [[], [], [], []]
aaa = None
for i in range(4):
    for j in range(4):
        while True:
            aaa = random.randint(1, 16)
            if aaa in generate_number:
                generate_number.pop(generate_number.index(aaa))
                break
        magic_square[i].append(aaa)

randomly_generated = [row[:] for row in magic_square]


# magic_square = [[14, 4, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]  # swapped one time
# magic_square = [[15, 4, 14, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]  # swapped two times
# magic_square = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]  # perfect magic square
def print_matrix(matrix):
    print('-' * 25)
    sum = 0
    print()
    for i in range(3, -1, -1):
        sum += matrix[abs(i - 3)][i]
    print('                    ', sum)
    print('                 ↗')

    for i in range(4):
        for j in range(4):
            aaa = matrix[i][j]
            if j == 0:
                print('|', end='')
            if aaa > 9:
                if j != 3:
                    print(aaa, end=' |')
                else:
                    print(aaa, end=' ')
                    sum = 0
                    for x in range(4):
                        sum += matrix[i][x]
                    print('==> ', sum)
            else:
                if j != 3:
                    print(aaa, end='  |')
                else:
                    print(aaa, end='  ')
                    sum = 0
                    for x in range(4):
                        sum += matrix[i][x]
                    print('==> ', sum)
        print()
    lis = [0, 0, 0, 0]
    print(' ⇓  ' * 4, '⇲')
    for i in range(4):
        for j in range(4):
            lis[j] += matrix[i][j]
    for i in lis:
        print(i, end='  ')
    sum = 0
    for i in range(4):
        sum += matrix[i][i]
    print('    ', sum)
    print('h = ', compute_violations(matrix))

    print('-' * 25)




def compute_violations(matrix):
    h = 0
    for i in range(4):
        sum = 0
        for j in range(4):
            sum += matrix[i][j]
        if sum != 34:
            h += 1
    lis = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            lis[j] += matrix[i][j]
    for i in lis:
        if i != 34:
            h += 1

    sum = 0
    for i in range(4):
        sum += matrix[i][i]
    if sum != 34:
        h += 1
    sum = 0
    for i in range(3, -1, -1):
        sum += matrix[abs(i - 3)][i]
    if sum != 34:
        h += 1
    return h


compute_violations(magic_square)


def done(matrix):
    # horizontal
    for i in range(4):
        sum = 0
        for j in range(4):
            sum += matrix[i][j]
        if sum != 34:
            return False
    # vertical
    lis = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            lis[j] += matrix[i][j]
    for i in lis:
        if i != 34:
            return False
    # diagonal L to R
    sum = 0
    for i in range(4):
        sum += matrix[i][i]
    if sum != 34:
        return False
    # diagonal R to L
    sum = 0
    for i in range(3, -1, -1):
        sum += matrix[abs(i - 3)][i]
    if sum != 34:
        return False
    return True


def swap_random_cells(parent_matrix):
    child_matrix = [row[:] for row in parent_matrix]
    aaa = random.randint(1, 16)
    b = random.randint(1, 16)
    while aaa == b:
        b = random.randint(1, 16)
    for i in range(4):
        for j in range(4):
            if parent_matrix[i][j] == aaa:
                child_matrix[i][j] = b
            elif parent_matrix[i][j] == b:
                child_matrix[i][j] = aaa
    h_of_parent_matrix = compute_violations(parent_matrix)
    h_of_child_matrix = compute_violations(child_matrix)
    if h_of_parent_matrix > h_of_child_matrix:
        return child_matrix
    else:
        return parent_matrix


t = time.time()
print('finding best square...')
sec = 0
while not done(magic_square) and time.time() - t <= 10:
    if round(time.time() - t) > sec:
        print(sec, end=' ')
        sec += 1
    magic_square = swap_random_cells(magic_square)

# print("\ngenerated magic square:")
# print_matrix(randomly_generated)
if not done(magic_square):
    print('more than 10 seconds to find a solution\nbest magic square to find is')
    print_matrix(magic_square)
    print('execution time is: 10s')
else:
    print_matrix(magic_square)
    print('execution time is: ', round(time.time() - t, 5), 's', sep='')
