# Trekanttall
def trekanttall(n):
    tn = n*(n+1)/2
    return tn


total = 0

for i in range(10):
    total += trekanttall(i)

print(total)

# Pseudokode

# SET total TO 0
# FOR hver i LESSER THAN 10
# INCREMENT total BY trekanttall(i)
# INCREMENT i BY 1
# REPEAT UNTIL i EQUAL TO 10
# DISPLAY total