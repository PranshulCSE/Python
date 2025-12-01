def sum(*args):
    s=0
    for item in args:
        s+=item

    return s

def details(**kwargs):
    print(kwargs)
    
details(Name='Pranshul',Age=22)

s=sum(4,8,6,54,72,94,6,24,25,4,55)
print(s)