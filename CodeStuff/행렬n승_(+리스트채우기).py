import copy

def mul_matrix(m1, m2):
    dup_m1 = copy.deepcopy(m1)
    m1 = [[0 for _ in range(len(m1))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                m1[i][j] += dup_m1[i][k] * m2[k][j]
    return m1


def pow_matrix(cur_mat, cnt):
    if cnt == 1 : return cur
    elif cnt == 2 : return mul_matrix(cur_mat, cur_mat)

    if cnt % 2 == 1 :
        tmp_mat = pow_matrix(cur_mat, (cnt-1) // 2)
        tmp_mat =  mul_matrix(tmp_mat, tmp_mat)
        return mul_matrix(tmp_mat, cur_mat)
    else :
        tmp_mat = pow_matrix(cur_mat, (cnt) // 2)
        return mul_matrix(tmp_mat, tmp_mat)

if __name__ == '__main__':
    cur = [[0.1, 0.2, 0.7], [0.4, 0.3, 0.3], [0.1, 0.1, 0.8]]
    print(pow_matrix(cur, 1000000000))

