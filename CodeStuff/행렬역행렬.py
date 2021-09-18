import copy


def det(list):
    return list[0] * list[3] - list[1] * list[2]

def mat_det_global(list):
    list_det = 0
    for i in range(3):
        input = []
        for j in range(1, 3):
            for k in range(0, 3):
                if i == k: continue
                input.append(list[j][k])
        if i != 1: list_det += list[0][i] * det(input)
        else: list_det -= list[0][i] * det(input)
    return list_det

def transpose(list):
    for i in range(3):
        for j in range(3):
            if j > i :
                tmp = list[i][j]
                list[i][j] = list[j][i]
                list[j][i] = tmp

def mat_det_local(list, n, m):
    list_det = 0
    transpose(list)
    for i in range(3):
        input = []
        for j in range(3):
            if n == j : continue
            for k in range(3):
                if k == m : continue
                input.append(list[j][k])
    return det(input)

if __name__ == '__main__':
    matrix = [[0.1, 0.2, 0.7], [0.4, 0.3, 0.3], [0.1, 0.1, 0.8]]
    ans = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            ans[i][j] = pow(-1, i + j) * mat_det_local(copy.deepcopy(matrix), i, j) / mat_det_global(matrix)

    for i in range(len(ans)):
        for j in range(len(ans)):
            print(ans[i][j], end= '\t')
        print()
