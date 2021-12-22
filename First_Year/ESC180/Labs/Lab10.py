def is_balanced(s):
    if(len(s) == 0):
        return True

    if all(elem == s[0] for elem in s):
        if(s[0] == "(" or s[0] == ")"):
            return False
        return True
    
    if(s[0] =="("):
        return is_balanced(s[1:]+"(")
    elif(s[0] ==")"):
        if(s[len(s) - 1] == "("):
            return is_balanced(s[1:len(s) - 1])
        else:
            return False

    return is_balanced(s[1:])
    

if __name__ == "__main__":
    print(is_balanced(")()("))