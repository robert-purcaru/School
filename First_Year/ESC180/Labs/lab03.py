import lab02

def sum_of_cubes(n):
    sum = 0
    for i in range (1, n + 1):
        sum += i * i * i
    return sum / 1.0

def sum_of_fancy_cubes(n):
    return (n**2 * (n + 1)**2) / 4

def check_sum(n):
    return sum_of_cubes(n) == sum_of_fancy_cubes(n)

def check_sums_up_to_n(N):
    for i in range (0, N):
        if(not check_sum(i)): 
            return False
    return True

def pi(n):
    sum = 0
    for i in range (0, n + 1):
        sum += ((-1)**i) / (2 * i + 1)
    return sum

if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")

    print(sum_of_cubes(3))
    print(sum_of_fancy_cubes(3))
    print(check_sum(5))
    print(check_sums_up_to_n(1001))
    print(pi(1000))