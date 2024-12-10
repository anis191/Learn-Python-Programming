def first(func):
    print("first start")
    func()
    print("first end")

def second():
    print("Second start")
    print("Second end")

first(second)