def get_current_value():
    global current_value
    print("Current value: " + str(current_value))

def add(to_add):
    global current_value, prev
    prev = current_value
    current_value += to_add

def subtract(to_subtract):
    global current_value, prev
    prev = current_value
    current_value -= to_subtract

def multiply(to_multiply):
    global current_value, prev
    prev = current_value
    current_value *= to_multiply

def divide(to_divide):
    global current_value, prev
    if (to_divide != 0):
        prev = current_value
        current_value /= to_divide
    else:
        print("does division by 0 look valid to you fucking piece of rye bread")
    
def mem(x):
    global memory
    memory = x

def recall():
    global current_value
    current_value = memory

def undo():
    global current_value, prev
    current_value, prev = prev, current_value

if __name__ == "__main__":
    current_value = 0
    memory = 0
    prev = 5
    print("Welcome to the calculator program.")
    print("Current value: " +  str(current_value))
    add(5)
    subtract(10)
    multiply(2)
    get_current_value()
    undo()
    get_current_value()
    undo()
    get_current_value()
    add(-5)
    get_current_value()
    divide(0)
    get_current_value()
    divide(94032843209842039859283475)
    get_current_value()
    multiply(94032843209842039859283475)
    get_current_value()
    
