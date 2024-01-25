import os
import jieba

one_gram = {

}

tow_gram = {

}


xk_dict = {

}
with open("xkjd/userdict.txt","r") as xk_file:
    for line in xk_file.readlines():

        word,code = line.strip().split("\t")
        if word not in xk_dict:
            xk_dict[word] = []
        xk_dict[word].append(code)

        xk_dict[word].sort(key=lambda x:len(x))

for root, dirs, files in os.walk("data",topdown=False):
    for name in files:
        print(os.path.join(root, name))
        with open(os.path.join(root, name),"r") as file:
            for line in file.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == "#":
                    continue
                try:
                    word,freq = line.strip().split("\t")
                    freq = int(freq)
                except:
                    print(line)
                if word in xk_dict:
                    code = xk_dict[word][0]
                else:
                    print(word,"不存在")
                    continue

                prev_char = None
                for char in code:
                    if char not in one_gram:
                        one_gram[char] = 0
                    one_gram[char] += freq
                    if prev_char is not None:
                        if (prev_char + char) not in tow_gram:
                            tow_gram[prev_char + char] = 0
                        tow_gram[prev_char + char] += freq
                    prev_char = char


with open("results/one_gram.txt","w") as file:
    for key,value in one_gram.items():
        file.write(key+"\t"+str(value)+"\n")


with open("results/tow_gram.txt","w") as file:
    for key,value in tow_gram.items():
        file.write(key+"\t"+str(value)+"\n")


