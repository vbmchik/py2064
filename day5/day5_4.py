from time import perf_counter


with open('advs.txt') as file_object:
    S = file_object.read()
#print(S)

S = ''.join( [x for x in S.lower() if x.isalpha() or x == ' '])
L = S.split(' ')
L = list(filter(lambda x: x != '', L))
U = set(L)
M = []
start_time = perf_counter()
for word in U:
    M.append((word, L.count(word)))
M = sorted(M, key = lambda x: x[1])
end_time = perf_counter()

print(f'Time taken: {end_time-start_time: 0.2f} seconds')
#print(M)
print(len(L))
