letter_list = []
with open("results/one_gram.txt","r") as file:
    for line in file.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == "#":
            continue
        char,freq = line.strip().split("\t")
        letter_list.append((char.upper(),int(freq)))
letter_list= sorted(letter_list,key=lambda x:x[1],reverse=True)
letters26 = []
instances26 = []
for (char,freq) in letter_list:
    letters26.append(char)
    instances26.append(freq)
print("letters26 = "   + str(letters26))
print("instances26 = "      + str(instances26))


two_map = {}
with open("results/two_gram.txt","r") as file:
    for line in file.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == "#":
            continue
        char,freq = line.strip().split("\t")
        char = char.upper()
        if char not in two_map:
            two_map[char] = 0
        two_map[char] += int(freq)
two_list = [(key,value) for key,value in two_map.items()]
two_list= sorted(two_list,key=lambda x:x[1],reverse=True)
bigrams = []
bigram_frequencies = []
for (char,freq) in two_list:
    bigrams.append(char)
    bigram_frequencies.append(freq)
print("bigrams = "   + str(bigrams) )
print("bigram_frequencies = "      + str(bigram_frequencies))
