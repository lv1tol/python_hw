import time
# === Decorator homework ===
def oneToMillion():
    for i in range(0,100000):
        if i % 2 == 0:
            print(i)

def deco(func):
    sTime = time.time()
    print("=----= Start =----=")
    func()
    print("=----= Finish =---=")
    print (time.time() - sTime, "seconds")

def fixNegativeParams(func):
    def wrapper(*args, **kwargs):
        newArgs = []
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                newArgs.append(1)
            else:
                newArgs.append(arg)

        newKwargs = {}
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                newKwargs[key] = 1
            else:
                newKwargs[key] = value

        return func(*newArgs, **newKwargs)

    return wrapper

@fixNegativeParams
def exFunction(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

deco(oneToMillion)

exFunction(10, -3, "red", -1, 200, key1=-5, key2="blue", key3=-100)