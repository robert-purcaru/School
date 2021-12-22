import numpy as np
import copy 


def print_matrix(M_lol):
    for r in M_lol:
        row = ""
        for c in r:
            row += "%7g" % c
        print(row)

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0: return i
    return i + 1

def rows(M):
    return len(M)


def cols(M):
    return len(M[0])


def get_row_to_swap(M, start_i):
    min_leading_row_index = start_i
    for i in range(start_i, rows(M)):
        if (get_lead_ind(M[i]) < get_lead_ind(M[min_leading_row_index])):
            min_leading_row_index = i
    return min_leading_row_index


def add_rows_coefs(r1, c1, r2, c2):
    ret = [0] * len(r1)
    for i in range(len(r1)):
        ret[i] = r1[i] * c1 + r2[i] * c2
    return ret

def eliminate(M, row_to_sub, best_lead_ind):
    if(M[row_to_sub][best_lead_ind] == 0):
        return M
    for row in range(row_to_sub+1, rows(M)):
        M[row] = sub(M[row], mult_const(mult_const(M[row_to_sub], 1/M[row_to_sub][best_lead_ind]), M[row][best_lead_ind]))
    return M


# `def eliminate(M, row_to_sub, best_lead_ind):
#     for c in range(len(M[row_to_sub])):
#         if(M[row_to_sub][c] == 0):
#             pass
#         else:
#             subCoef = M[row_to_sub][c]
#             break
#     sto = None
#     Free = False
#     for r in range(best_lead_ind, len(M)):
#         for c in range(len(M[r])):
#             if(M[r][c] == 0 and not Free):
#                 pass
#             elif(sto == None):
#                 sto = M[r][c]
#                 Free = True
#                 M[r][c] = (M[r][c] - M[row_to_sub][c] * (M[r][c] / subCoef))
#             else:
#                 M[r][c] = (M[r][c] - M[row_to_sub][c] * (M[r][c] / subCoef))
#         sto = None
#         Free = False
#     return M


def sub(L1, L2):
    ret = []
    for i in range(len(L2)):
        ret.append(L1[i] - L2[i])
    return ret

def mult_const(L, k):
    ret = []
    for i in range(len(L)):
        ret.append(L[i]*k)
    return ret
    
def backward_step(M):
    for row in range(rows(M)-1, -1, -1):
        c = get_lead_ind(M[row])
        if (M[row][c] != 0):
                M[row] = mult_const(M[row], 1/M[row][c])
        for active_row in range(row-1, -1, -1):
            M[active_row] = sub(M[active_row], mult_const(M[row], M[active_row][c]/M[row][c]))
    return M

def forward_step(M):
    for r in range (rows(M)):
        ind = get_row_to_swap(M, r)
        M[ind], M[r] = M[r], M[ind]
        M = eliminate(M, r, get_lead_ind(M[r]))
    return M

def ge(M):
    M = forward_step(M)
    M = backward_step(M)
    return M

def solve(M, b):
    aug = copy.deepcopy(M)
    for r in range(rows(M)):
        aug[r].append(b[r])
    return ge(aug)

if __name__ == "__main__":


    M1 = [[1, 2, 3],
        [4, 5, 6]]
    
    M2 = [[5, 6, 7, 8],
        [0, 0, 0, 1],
        [0, 1, 5, 2],
        [0, 0, 0, 0]]
        
    M3 = [[5, 6, 7, 8],
        [0,0, 1, 1],
        [0, 0, 5, 2],
        [0, 0, 7, 0]]
    
    #print_matrix(eliminate(M3, 1, 2))

    M4 = [[ 1, -2, 3, 22 ],[ 0, 16, -8, 248 ],[ 0, 0, 3.5, -38.5]]

    M5 = [[ 0, 0, 1, 0, 2,],
        [ 1, 0, 2, 3, 4,],
        [ 3, 0, 4, 2, 1,],
        [ 1, 0, 1, 1, 2,]]
    
    M6 = [[ 1, 0, 2, 3, 4,],
        [ 0, 0, 1, 0, 2,],
        [ 3, 0, 4, 2, 1,],
        [ 1, 0, 1, 1, 2,]]

    M7 = [[ 1, -2, 3, 22],
        [ 3, 10, 1, 314],
        [ 1, 5, 3, 92]]


    #print_matrix(backward_step(M4))
    
    # print_matrix(add_rows_coefs(M1[0], 2, M1[1], 1))
    #print_matrix(eliminate(M6, 0, 0))

    M8 = [[1, 2],[3, 4]]
    b8 = [2,1, 7, 2]
    # print_matrix(solve(M7, b8))
    print_matrix(ge(M7))