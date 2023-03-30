arr = []
with open("mc5/log.mcnvt.txt") as f:
    for line in f:
        #print(float(x) for x in coloumn.split())
        arr.append(line.split())
        
probs = []
for i in range(74, 114):
    probs.append(float(arr[i][6]))

prob = 0.0
idx = 0
for k in probs:
	prob+= k
	idx += 1

print(prob/idx)
