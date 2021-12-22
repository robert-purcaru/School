import numpy as np
import math

# ESC180 Final Examination, Fall 2020
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam except
# to ask questions on Piazza.
#
# You may ask questions on the course Piazza. Please make your question private
# if it must disclose part of the solution. Otherwise, please make it public.
# Please check Piazza occasionally in case there are announcements or
# clarifications.
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes. Late submissions will only be accepted from students who
# have been preapproved for a time extension through accessibility services.
#
# To be eligible to receive partial credit, you must submit a file which does
# not produce an error when read into Python. Any code that you know produces
# errors must be commented out. By themselves, comments/docstrings will not
# earn any points. However, they may help TAs in deciding how to award
# partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#

################################################################################

#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.

def most_common_frequent_word(files):
    most_freq = {}
    removeables = [".", ",", "!", "?", "-", "\\n"]
    for file in files:
        f = open(file) 
        text = f.read().lower()
        for item in removeables:
            text = split_string_at_e(text, item)
        text_list = text.split()
        frequency_in_file = make_frequency_map(text_list)
        most_freq_in_file = largest_value_in_map(frequency_in_file)  
        add_to_map(most_freq, most_freq_in_file)      
        f.close()

    most_common_word = largest_value_in_map(most_freq)
    return most_common_word[0]

def add_to_map(M, T):
    if (T[0] in M):
        M[T[0]] = M[T[0]] + 1
    else:
        M[T[0]] = 1

def make_frequency_map(S):
    counter = {}
    for word in S:
        if(word in counter):
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    return counter

def largest_value_in_map(M):
    largest_value = -1
    largest_key = ""
    for key in M:
        if(M[key] > largest_value):
            largest_value = M[key]
            largest_key = key
    return (largest_key, largest_value)
        

def split_string_at_e(text, e):
    return text.replace(e, "")


#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}


def get_links(html_text):
    links = {}
    for i in range(len(html_text)):
        try:
            if html_text[i:i+7] == "<a href":
                local_text = html_text[i:]
                local_text = local_text.split("=", 1)
                local_text[1] = local_text[1].split("</a>", 1)[0]
                local_text = local_text[1].split("\"", 2)
                for e in local_text:
                    if e == " ":
                        local_text.remove(e)
                link = local_text[0]
                name = local_text[1]
                name = name[1:]
                links[name] = link
        except:
            break
    return links

###############################################################################

#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be


# I'm going to assume that n is a list of numbers with length n.
# This function is kinda similar to the sum_list function in one the of examples we got I think. It computes the sum of the list n by breaking it in half until it reaches a list of length 0 or whatever element of the list, at which point the value begins to move up the call stack, since the worst case is every case where a tree of depth log_2 n + 1 is made, the log term is justified. As we go down the tree (the 'tree' being inverted with the base at the top, more like a funnel I guess) the runtime complexity of each layer is proportional to (n/l+1) where l is the layer from the bottom, with the initial call having a runtime complexity of 0. This is true because each call critically does not take the same amount of time to run, insted being related to the layer that its on. As was explained in the document that had the similar function, each layer expands out to have a runtime complexity of kn, in the case that was presented. excluding the direct_sum line, this is the same logic as the example presented in the review with complexity n * log(n). Adding the direct_sum line, we perform a side sum that does nothing to the process except waste time proportional to the n that is passed to it. Since this n is is related to origional n that was passed in and the opperation is performed separetly every iteration of the stack, the overall time complexity is the product of the first complexity with the the time complexity of the direct_sum. The direct function is time complexity O(n) since it creates a direct stack (not a tree) that collapses linearly. Therefore the overall time complexity is O(n^2 * log(n))
 
def f(n):
    if(len(n) == 0):
        return 0
    if(len(n == 1)):
        return n[1]

    direct_sum(n)

    mid = len(n) // 2
    return f[:mid] + f[mid:] 



def direct_sum(n):
    if len(n) == 1:
        return n[0]
    return n[0] + direct_sum[1:]
    


###############################################################################




###############################################################################
#  Problem 4 (15 pts)
#
#  This problem will be auto-graded.
#
#
#  It is possible to combine the numbers 1, 5, 6, 7 with arithemtic operations
#  to get 21 as follows: 6/(1-5/7).
#
#  Write a function that takes in a list of three numbers and a target number, and
#  returns a string that contains an expression that uses all the numbers
#  in the list once, and results in the target. Assume that the task is possible
#  without using parentheses.
#
#  For example, get_target_noparens([3, 1, 2], 7) can return "2*3+1" or "1+2*3"
#  (either output would be fine).
#
#

def get_target_noparens(nums, target):
    a = nums[0]
    b = nums[1]
    c = nums[2]

    combinations = [[a, b ,c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]

    for case in combinations:
        if(case[0] + case[1] + case[2] == target):
            return str(case[0]) + "+" + str(case [1]) + "+" + str(case[2])
        if(case[0] + case[1] - case[2] == target):
            return str(case[0]) + "+" + str(case[1]) + "-" + str(case[2])
        if(case[0] + case[1] * case[2] == target):
            return str(case[0]) + "+" + str(case [1]) + "*" + str(case[2])
        if(case[0] + case[1] / case[2] == target):
            return str(case[0]) + "+" + str(case[1]) + "/" + str(case[2])

        if(case[0] - case[1] + case[2] == target):
            return str(case[0]) + "-" + str(case [1]) + "+" + str(case[2])
        if(case[0] - case[1] - case[2] == target):
            return str(case[0]) + "-" + str(case[1]) + "-" + str(case[2])
        if(case[0] - case[1] * case[2] == target):
            return str(case[0]) + "-" + str(case [1]) + "*" + str(case[2])
        if(case[0] - case[1] / case[2] == target):
            return str(case[0]) + "-" + str(case[1]) + "/" + str(case[2])

        if(case[0] * case[1] + case[2] == target):
            return str(case[0]) + "*" + str(case [1]) + "+" + str(case[2])
        if(case[0] * case[1] - case[2] == target):
            return str(case[0]) + "*" + str(case[1]) + "-" + str(case[2])
        if(case[0] * case[1] * case[2] == target):
            return str(case[0]) + "*" + str(case [1]) + "*" + str(case[2])
        if(case[0] * case[1] / case[2] == target):
            return str(case[0]) + "*" + str(case[1]) + "/" + str(case[2])

        if(case[0] / case[1] + case[2] == target):
            return str(case[0]) + "/" + str(case [1]) + "+" + str(case[2])
        if(case[0] / case[1] - case[2] == target):
            return str(case[0]) + "/" + str(case[1]) + "-" + str(case[2])
        if(case[0] / case[1] * case[2] == target):
            return str(case[0]) + "/" + str(case [1]) + "*" + str(case[2])
        if(case[0] / case[1] / case[2] == target):
            return str(case[0]) + "/" + str(case[1]) + "/" + str(case[2])

################################################################################
#  Problem 5 (15 pts)
#
#  Up to 3 pts will be awarded for making progress toward a solution.
#
#  Now, write the function get_target which returns a string that contains an
#  expression that uses all the numbers in the list once, and results in the
#  target. The expression can contain parentheses. Assume that the task is
#  possible.
#  For example, get_target([1, 5, 6, 7], 21) can return "6/(1-5/7)"


# I think the way to go about this one is to break it up into recurssive opperations that call back with a new target for every operation that could be removed on the elements of the set minus whichever is being tested. so if the numbers were for example [1,2,3,4] and the target was 5, you'd try to see if you could make 5 - 1 with [2,3,4] and your solution would involve 1 + "the solution you get with [2,3,4] for taget 4". The brute force way is to just try every combination and see where you get the target over and over again. I don't think my implemenation works though

def get_target(nums, target):
    if(len(nums) == 1):
        return nums
    for i in range(len(nums)):
        if(nums[i] + get_target(nums.pop(i)) == target - nums[i]): # I think you do something like this for each opperation where you check to see if you can hit a new target that's the inverse of whatever operation you initially specify (on the left)
            return target
    return target


################################################################################


if __name__ == "__main__":
    print(most_common_frequent_word(["sample.txt"]))
    name = "hello"
    print(get_links('baksaflj, <a href = "http://engsci.utoronto.caca">EngSci PAGE</a>fdsofjosdf dsf <a href = "http://engsci.utoronto.ca">EngSci homepage</a> f  <a href = "http://engsci.utorongdfgdfgto.caca">EnsdagSci PAGE</a>dsa'))

    print(get_target_noparens([10,15,1], 149))
    pass

    

