lists = [
    [1,2,3],
    ['a','b','c'],
    [1,1,1]
]

# создать из исходного списка новый такой что все элементы долюны быть числами и суммма всех чисел списка больше 4


t = [True, False, True, False, False, True]


res = [x for x in lists if all([isinstance(item, int) for item in x]) and sum(x)>4 ]

res1 = list(
    filter(
        lambda x: all([isinstance(item, int) for item in x]) and sum(x)>4,
        lists
    )
    )
res2 = [ x for x in lists if all(map(lambda t: isinstance(t,int),x)) and sum(x) > 4 ]
print(res)
print(res1)
print(res2)