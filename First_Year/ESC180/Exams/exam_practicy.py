def insert(L, e):
    L.append(e)
    return sorted(L)

# def select_gifts(good_ratings, want_ratings):
#     adjusted_map = {}
#     for key in good_ratings:
        
#         good_value = good_ratings[key]
#         want_value = 0

#         if(key in want_ratings):
#             want_value = want_ratings.get(key)
#             want_ratings.pop(key)

#             print(want_value)
#             print(good_value)
        
#         if(good_value + want_value in adjusted_map):
#             adjusted_map{(good_value + want_value) : []}
#             print(adjusted_map)
#         adjusted_map[good_value + want_value].append(key)
        
#     for key in want_ratings:
#         want_value = want_ratings[key]
#         if(good_value + want_value in adjusted_map):
#             adjusted_map[want_value] = []
#         adjusted_map[want_value].append(key)

#     largest = 0
#     for key in adjusted_map:
#         if(key > largest):
#             largest = key
    
#     return adjusted_map[key].sort()
        

def transpose(matrix):
    rows, cols = (len(matrix), len(matrix[0])) 
    arr=[] 
    for i in range(cols): 
        col = [] 
    for j in range(rows): 
        col.append(0) 
        arr.append(col) 
    print(arr) 
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print('i: ', i)
            print('j: ',  j)
            arr[j][i] = (matrix[i][j])
            print(arr)
    return arr

def is_sorted(L):
    if len(L) <= 1:
        return True
    check = 0
    for i in range(len(L) - 1):
        if(L[i] - L[i+1] != 0 and check == 0):
            check = L[i] - L[i+1]
        if(check * (L[i]- L[i+1]) < 0):
            return False
    return True

def euc_distance(u, v):
    dist = 0
    for i in range(max([max(u.keys()), max(v.keys())]) + 1):
        dist = dist + (u.get(i, 0) - v.get(i, 0))**2
    dist = dist**0.5
    return dist

def get_year(str):
    year = 0
    try:
        year = int(str[0:4])
    except:
        year = -1
    
    return year


def movies_by_release_date(movies):
    ret = {}
    for key in movies:
        
        if(get_year(movies.get(key)) in ret):
            # ret.update({get_year(movies.get(key)) : ret[get_year(movies.get(key))].append(key)})
            print(ret[get_year(movies.get(key))])
            ret.update({get_year(movies.get(key)) : [key].extend([ret[get_year(movies.get(key))]])})
        else:
            ret.update({get_year(movies.get(key)) : [key]})
    return ret


def merge(L1, L2):
    if(len(L1) == 1):
        return L2
    if(len(L2) == 1):
        return L1

    if(L1[0] <= L2[0]):
        return [L1] + (merge(L1[1:], L2))
    elif(L1[0] > L2[0]):
        return [L2] + (merge(L1, L2[1:]))

def filter_out_odds(L):
    if(len(L) == 1):
        if(L[0] % 2 == 1):
            return []
        else:
            return [L[0]]
    if(L[0] % 2 == 1):
        return filter_out_odds(L[1:])
    else:
        return [L[0]] + (filter_out_odds(L[1:]))


def most_productive_elf(toys_produced):
    highest_value = max(toys_produced.values())

    for key in toys_produced:
        if toys_produced[key] == highest_value:
            return key

    return -1

def two_smallest(L):
    ret = [0, 0]
    ret[1] = min(L)
    L.remove(min(L))
    ret[0] = min(L)
    return ret

def largest_col_sum(M):
    largest_sum = -1000000
    for i in range(len(M[0])):
        sum = 0
        for j in range(len(M)):
            sum = sum + M[j][i]
            if sum > largest_sum:
                largest_sum = sum
    
    return largest_sum

def f(d):
    d1 = {}
    for k in d:
        d1[k] = d[k]
    return d1

if __name__ == "__main__":
    # print(insert([2.4, 2.1, 21.3], 2.3))
    good_ratings = {"Calc textbook": 5, "iPhone": 1, "Alarm clock": 4, "Notebooks": 4}
    want_ratings = {"iPhone": 4, "A+ in CSC": 5, "Calc textbook": 4, "Notebooks": 5}
    # select_gifts(good_ratings, want_ratings)
    M = [[5, 6, 7], [0, -3, 5]]
    # print(transpose(M))
    # print(euc_distance({1:4, 2:5, 4:100}, {1:4, 2:5, 5:100}))
    # print(movies_by_release_date({"Dude, Where’s My Death Star": "a long time ago, in a galaxy far far away",
    # "Star Wars: The Force Awakens": "2015, in Los Angeles",
    # "Star Wars": "1977, in Los Angeles",
    # "Sleepless in Aldera": "a long time ago, in Alderaan City",
    # "Jurassic World": "2015, in New York"}))

    # print(merge([4, 8, 10], [2, 5]))
    # list1 = [1, 2]
    # list1.append(1)
    # print(list1)

    # print(filter_out_odds([5,-2,4,0,3,7,8]))

    # print(most_productive_elf({"Bob":4000, "Gloria":7000, "Hugo":6000, "Grumbles":42}))

    # print(two_smallest([5, 3, 10, 4]))
    # print(largest_col_sum( [ [1, 2, 3, 4], [5, 0, 5, 0], [6, 7, 8, 9]]))


    d = {1:[[1, 2]], 0:[[3, 4]]}
    d1 = f(d)
    d1[0][0][0] = 5
    print(d[0])



