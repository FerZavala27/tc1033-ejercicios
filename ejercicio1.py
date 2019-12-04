def greet():
    name = input()
    print("Hello", name)
greet()

def run(num):
    num=int(input())
    if num>=0 and num<10:
        for x in (0, num):
            print("runnung")
