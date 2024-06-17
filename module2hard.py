def password(n):
    pairs = []
    used = set()
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append(f'{i}{j}')
                used.add(i)
                used.add(j)
    return ''.join(pairs)
for n in range(3, 21):
    result = password(n)
    print(f'{n}: ', result)
