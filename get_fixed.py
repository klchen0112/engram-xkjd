from itertools import permutations


base = ['K','T','Q','F','B','P','K','J','E']
print("fixed_letter_lists1 = [")
for kb_perm in permutations(["K","B","Q"]):
    base[0] = kb_perm[0]
    base[2] = kb_perm[1]
    base[3] = kb_perm[2]
    for pke_perm in permutations(["P","K","E"]):
        base[5] = pke_perm[0]
        base[6] = pke_perm[1]
        base[8] = pke_perm[2]
        print(base,",")
print("]")

print("fixed_letter_index_lists1 = [")
fixed_list = [1,2,3,4,5,8,10,11,12]
for i in range(36):
    print(fixed_list,",")
print("]")


print("open_letter_index_lists1 = [")
open_list = [0,6,7,9,13,14,15]

for i in range(36):
    print(open_list,",")
print("]")


print()
print()
print("fixed_letter_index_lists3 = [")
open_list = [2, 4,5,6,7, 13,16,17,18]
for i in range(36):
    print(open_list,",")
print("]")
