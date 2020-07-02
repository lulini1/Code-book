#      SEND
#   +  MORE
# ----------
#     MONEY

p = list(__import__("itertools").permutations(range(10), 8))
r = list()

while(p):
    i = p.pop()
    if not i[6] or not i[2]: continue
    if   1 * (i[0] + i[1] - i[7]) + \
        10 * (i[3] + i[5] - i[1]) + \
       100 * (i[1] + i[4] - i[3]) + \
      1000 * (i[6] + i[2] - i[4]) + \
     10000 * (  0  +   0  - i[2]): continue
    r.append({'D' : i[0], \
              'E' : i[1], \
              'M' : i[2], \
              'N' : i[3], \
              'O' : i[4], \
              'R' : i[5], \
              'S' : i[6], \
              'Y' : i[7]})

for i in range(len(r)):
    print("Solution 1: ")
    for j in range(len(r[i])):
        print(f"  {list(r[i].keys())[j]} = {list(r[i].values())[j]}")
    print("")
print(i + 1, "solution(s) found. ")