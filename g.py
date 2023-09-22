
dick = {str(k): k ** 2 for k in range(1, 10)}
print(dick)

def dict_print(arg=0, **kwargs):
    print(arg)
    print(kwargs)

dict_print(9, **dick)
