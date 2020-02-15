def read_file(filepath):
    f = open(filepath,errors='ignore')
    data = f.read()
    f.close()
    return data

def vowel_counter(file):
    data = read_file(file).lower()
    vowels = 'aeiou'
    total_vowels = 0
    for item in vowels:
        total_vowels+=data.count(item)
    return total_vowels

def vowel_counter_enhanced(file):
    vow={}
    data = read_file(file).lower()
    vowels = 'aeiou'
    for item in vowels:
        vow[item]=data.count(item)
    return vow


# calling the function vowel_counter
# file = 'data/Richardson_Clarissa.txt'
# t_v=vowel_counter_enhanced(file)
# for vowels in t_v:
#     print('The number of',vowels,'in data are',t_v[vowels])


# # calling function 1
# file = 'data/Richardson_Clarissa.txt'
# content = read_file(file)
# print("total chars :", len(content))

# # calling function 1
# content = read_file('data/Sterne_Sentimental.txt')
# print("total chars in second file :", len(content))