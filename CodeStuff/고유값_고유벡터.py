import copy

import numpy as np

def getEigenVal(list):
    ans = []
    for l in np.arange(-1000, 1000, 0.1):
        l = round(l, 1)
        det_val = 0
        for i in range(0, 3):
            tmp = []
            for n in range(1, 3):
                for m in range(0, 3):
                    if m == i: continue
                    if n == m:
                        tmp.append(round(list[n][m] - l, 1))
                    else:
                        tmp.append(round(list[n][m], 1))
            if i == 0:
                det_i = round(round(list[0][i] - l, 1) * (round(tmp[0] * tmp[3], 2) - round(tmp[1] * tmp[2], 2)), 3)
            else:
                det_i = round(round(list[0][i], 1) * (round(tmp[0] * tmp[3], 2) - round(tmp[1] * tmp[2], 2)), 3)
            if i % 2 == 0:
                det_val = round(det_val + det_i, 3)
            else:
                det_val = round(det_val - det_i, 3)
        if det_val == 0:
            ans.append(l)

    return ans

def gcd(n, m):
    return n if m ==0 else gcd(m, n % m)

def linearOperation(list, colMat):
    for n in range(len(list)):
        sum = 0
        for m in range(len(list[n])):
            sum += round(list[n][m] * colMat[m], 1)
        if sum != 0 : return False
    return True

def getEigenMat(eigenVal,targetMat):
    ans = []
    for val in eigenVal:
        flag = False
        for i in range(len(targetMat)):
            targetMat[i][i] = round(targetMat[i][i]-val, 1)
        for i in range(-50, 50):
            for j in range(-50, 50):
                for k in range(-50, 50):
                    if i ==0 and j==0 and k==0 : continue
                    if linearOperation(targetMat, [i, j, k]):
                        flag = True; ans.append([i, j, k]); break
                if flag: break
            if flag: break
        for i in range(len(targetMat)):
            targetMat[i][i] = round(targetMat[i][i]+val, 1)

    for el in ans:
        gcd_val = abs(el[0])
        for i in range(1, len(el)):
            gcd_val  = gcd(gcd_val, abs(el[i]))
        ## 최대공약수로 나눈다
        for i in range(len(el)):
            ans[ans.index(el)][i] /= gcd_val
        ## 전부음수인 경우, 양수로 바꾼다
        tmp = el[0]; flag = True
        for i in range(1, len(el)):
            if el[i] * tmp < 0 : flag = False
        if flag:
            for i in el: ans[ans.index(el)][el.index(i)] = abs(ans[ans.index(el)][el.index(i)])

    return ans

if __name__ == '__main__':
    M = [[0.1, 0.2, 0.7], [0.4, 0.3, 0.3], [0.1, 0.1, 0.8]]
    eigenVal = getEigenVal(copy.deepcopy(M))
    eigenMat = getEigenMat(eigenVal, M)
    print(eigenVal)
    print(eigenMat)