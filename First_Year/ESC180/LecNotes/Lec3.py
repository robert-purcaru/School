'''This is a docstring'''

def set_grade_zero():
    global grade
    grade -=98

def try_set_grade_zero():
    grade = 0

def make_global():
    global a
    a = 5

if __name__ == '__main__':
    grade = 98
    try_set_grade_zero()
    print(grade)
    set_grade_zero()
    print(grade)

    make_global()
    print(a)

    a, b, c = "123", "456", "789"

    print(a + b + c)

    a, b = b, a

    print(a + b + c)

    #a = a + b
    #b = a - b
    #a = a - b