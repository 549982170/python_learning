import itertools

a = [1, 2, 3, 4]
for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
    print p

for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1)):
    print subset