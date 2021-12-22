import urllib.request
import pyserial
 

def initialize_file(fileName):
    return open(fileName, encoding="utf8").read().split()


def count_words(text):
    map = {}
    for word in text:
        if not word in map.keys():
            map[word] = 1
        else:
            map[word] += 1
    return map

def top10(L):
    return sorted(L)[-10:] 

def invert_map(m):
    inv_freq = {}
    for key, value in m.items():
        if not value in inv_freq.keys():
            inv_freq[value] = [key]
        else:
            inv_freq[value].append(key)
    return inv_freq

def top10_freq(m):
    top = []
    for value in m:
        for word in value[1]:
            if len(top) > 10:
                return top
            top.append(word)
    return None

def get_top_10_file(file):
    literature = initialize_file(file)
    freq = count_words(literature)
    inv_freq = invert_map(freq)
    inv_freq = sorted(inv_freq.items())[::-1]
    print(top10_freq(inv_freq))

def get_search_results(term):
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p="+term)
    page = f.read().decode("utf-8")
    f.close()
    end_index = page.find(" results</span>")
    begin_index = end_index - 14 + page[end_index-20:end_index].find("<span>")
    val = page[begin_index:end_index]
    #return (val)
    return int(val.replace(" ", "").replace(",", ""))

def choose_variant(variants):
    greatest_index = 0
    greatest = -1
    for i in range(len(variants)):
        print(get_search_results(variants[i]))
        if get_search_results(variants[i]) > greatest:
            greatest = get_search_results(variants[i])
            greatest_index = i 

    return variants[greatest_index]

if __name__ == '__main__':
    print(get_top_10_file("literature.txt"))
    call = ["top+ranked+school+uoft", "top+ranked+school+waterloo"]
    print(choose_variant(call))