import pickle
import time

'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    top_sum = 0
    square_sum1 = 0
    for key in vec1:
        if key in vec2:
            top_sum += vec1[key] * vec2[key]

    return (top_sum) / (norm(vec1) * norm(vec2))




def build_semantic_descriptors(sentences):
    d = {}
    # for sentence in sentences:
    #     for word in sentence:
    #         if word in d:
    #             for other_word in sentence:
    #                 if other_word != word:
    #                     d[word][other_word] += 1
    #         else:
    #             for other_word in sentence:
    #                 if other_word != word:
    #                     d[word][other_word] = 1
    for sentence in sentences:
        for word in sentence:
            d[word] = d.get(word, {})
        for word in sentence:
            for key in d.keys():
                if key != word and key in sentence:
                    d[key][word] = d[key].get(word, 0) + 1
    return d

def build_semantic_descriptors_from_files(filenames):
    terminating = [".", "?", "!"]
    sentences = []
    for file in filenames:
        content = open(file, "r", encoding="latin1")
        content = content.read()
        content = remove_non_terminating(content)
        start_ind = 0
        for i in range(len(content)):
            if content[i] in terminating or i == len(content) - 1:
                sentences.append(content[start_ind: start_ind + i].split(" "))
                start_ind = i + 1
    return build_semantic_descriptors(sentences)    

def remove_non_terminating(string):
    non_terminating = [",", "-", "--", ":", ";", "\""]
    string = string.replace("\n", " ")
    for punc in non_terminating:
        string = string.replace(punc, "")
    return string

# def split_around(content, char):
#     ret = []
#     if (type(content) == list):
#         for sentence in content:
#             sentence.split(char)
#             for new_sentnece in sentence:
#                 ret.append(new_sentnece)       
#     else:
#         content = content.split(char)
#         for new_sentnece in content:
#             ret.append(new_sentnece)    
#     return ret


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_similarity = 0
    good_word = ""
    for choice in choices:
        similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        if(similarity >  max_similarity):
            good_word = choice
            max_similarity = similarity

    return max_similarity

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    content = open(filename, "r", encoding="latin1")
    content = content.read()
    questions = content.split("\n")
    num_answers = len(questions)
    num_correct = 0
    for question in questions:
        question = question.split(" ")
        word = question[0]
        answer = question[1]
        choices = question[2:]
        try:
            guessed = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
            if guessed == answer: 
                num_correct += 1
        except:
            pass
    return num_correct/num_answers

def save_dict(d, filename):
    with open(filename, 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

def open_dict(filename):
    with open(filename, 'rb') as handle:
        return(pickle.load(handle))

if __name__ == "__main__":
    # short1 = {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}
    # short2 = {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}

    # cos_sim_test1 = {"a": 1, "b": 2, "c": 3}
    # cos_sim_test2 = {"b": 4, "c": 5, "d": 6}
    # #print(cosine_similarity(cos_sim_test2, cos_sim_test1))
    # sentences = [["i", "am", "a", "sick", "man"],
    #              ["i", "am", "a", "spiteful", "man"],
    #              ["i", "am", "an", "unattractive", "man"],
    #              ["i", "believe", "my", "liver", "is", "diseased"],
    #              ["however", "i", "know", "nothing", "at", "all", "about", "my",
    #                         "disease", "and", "do", "not", "know", "for", 
    #                         "certain", "what", "ails", "me"]]
    # build_test = "1.2.3.4?5?5?6!5.1.3.4!"

    
    start = time.time()
    sd = (build_semantic_descriptors_from_files(["WarAndPeace.txt"]))
    print(time.time()-start)
    save_dict(sd, "dict.pickle")
    #sd = open_dict("dict.pickle")
    print(run_similarity_test("test.txt", sd, cosine_similarity))
    
