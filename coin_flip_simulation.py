import random
coin = ("T", "H")

for i in range(10):
    consecutive = 0
    last = -1
    flips = []

    while consecutive < 3:
        toss = random.randint(0, 1)
        flips.append(coin[toss])
        if toss == last:
            consecutive += 1
        else:
            consecutive = 1
            last = toss
    print("".join(flips))
    print(len(flips), "flips to get 3 consecutive", coin[last])
# this one was too dificult i need to look for it in the internet, damn it
