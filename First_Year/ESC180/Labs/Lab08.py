

def problem_1(file_name):
    file = open(file_name, encoding="uft-8", errors='ignore')
    text = file.read()
    
    lines = text.split("\n")

    for line in lines:
        if line.lower().find("lol") != -1:
            print(line)

def dict_to_str(d):
    ret = ""
    for key, val in d.items():
        ret += str(key) + ", " + str(val) + "\n"
    return ret
    
def dict_to_str_sorted(d):
    ret = ""
    for key in sorted(d.keys()):
        ret += str(key) + ", " + str(d[key]) + "\n"
    return ret


def get_dictionary(file_name):
    file = open(file_name)
    text = file.read()
    lines = text.split("\n")

    dictionary = {}
    for line in lines:
        split_line = line.split("  ")
        if len(split_line) > 1:
            dictionary[split_line[0]] = split_line[1].split(" ")
    
    return dictionary
    
def get_sounds(file_name):
    file = open(file_name)
    text = file.read()
    lines = text.split("\n")

    dictionary = {}
    for line in lines:
        split_line = line.split("\t")
        if len(split_line) > 1:
            dictionary[split_line[0]] = split_line[1]
    return dictionary  


def num_vowels(word):
    global word_dict, phone_dict
    phones = word_dict[word]
    num_vowels = 0
    for phone in phones: 
        for phone_entry in phone_dict.keys():
            if phone_entry in phone:
                if phone_dict[phone_entry] == "vowel":
                    num_vowels -= -1
    
    return num_vowels

def total_syllables(text):
    syllables = 0
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("-", " ")
    
    words = text.split(" ")
    for word in words:
        syllables += num_vowels(word)
    return syllables

def readability(text):
    total_words = len(text.split(" "))
    total_sentences = len(text.split(". ")) + len(text.split("? ")) + len(text.split("! "))
    total_speak = total_syllables(text)
    return 0.39 * (total_words / total_sentences) + 11.8 * (total_speak / total_words) - 15.59

if __name__ == "__main__":
    word_dict = get_dictionary("cmu_vowels.txt")
    print(word_dict)
    phone_dict = get_sounds("noises.txt")
    #print(num_vowels(""))
    print(readability("FLESCH KINCAID READABILITY GRADE."))

