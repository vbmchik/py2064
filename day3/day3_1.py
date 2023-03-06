# methods ( *args, **vargs )

def sum( *args: int )->int:
    s = 0
    for a in args:
        s += a
    print(args)
    return s

def sum1( **args ):
    for key, value in args.items():
        print(key, value)
    if "mi" in args.keys():
        print(args["mi"])
    print(args)
    
print(sum(1,2,3,4,5))
print(sum(2,3))
sum1(r=4,mi=9,atlas=12)
sum1(**{"key1":2, "key2":3})