import random

s = "abcdef123"

#print(''.join(random.sample(s, len(s))))

s = list(s)
random.shuffle(s)
print("".join(s))
