#1
def list1_starts_with_list2(list1, list2):
    if(len(list1) >= len(list2)):
        for i in range(0, len(list2)):
            if(list1[i] != list2[i]):
                break
            if(i == len(list2) - 1):
                return True
    return False

#2
def match_pattern(list1, list2):
    for i in range(0, len(list1) - len(list2) + 1):
        for j in range(0, len(list2) + 1):
            if(j == len(list2)):
                return True
            if(list1[i + j] != list2[j]):
                break
    return False

#3
def repeats(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]: 
            return True
    return False

#4a
def shape(M):
    rows = len(M)
    cols = len(M[0])
    return rows, cols

#4b
def mult_M_v(M, v):
    res = [0] * len(v)
    for c in range(0, len(v)):
        for r in range(0, len(M[0])):
            res[c] += M[c][r] * v[c]
    return res

#4c
def mult(M1, M2):
    rows1, cols1 = shape(M1)
    rows2, cols2 = shape(M2)
    #ret = [[0]*cols2]*rows1 causes error
    ret = zero_mat(rows1, cols2)
    for c in range(cols2):
        for r in range(rows1):
            k = dot(get_row(M1, r), get_col(M2, c))
            ret[r][c] = k
    return ret

def zero_mat(rows, cols):
    ret = []
    for r in range(rows):
        ret.append([0]*cols)
    return ret

def get_row(M, r):
    return M[r]

def get_col(M, c):
    ret = [0]*len(M)
    for r in range(len(ret)):
        ret[r] = M[r][c]
    return ret   

def dot(v1, v2):
    res = 0
    for i in range(0, len(v1)):
        res += v1[i]*v2[i]
    return res

if __name__ == '__main__':
    print(list1_starts_with_list2([1, 2, 3], [1, 2]))
    print(match_pattern([1, 2, 3, 4], [3, 4]))
    print(repeats([1, 2, 3, 5, 4]))

    M1 = [[1, 0, 1], 
          [0, 1, 2]]
    M2 = [[2, 3, 3], 
          [4, 5, 1],
          [1, 2, 1]]
    print(mult(M1, M2))
