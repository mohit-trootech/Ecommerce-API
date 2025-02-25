arg = int(input("Enter Number: "))
try:
    for unit in ["", "K", "M"]:
        if abs(arg) < 1000.0:
            print(f"{arg:6.2f}{unit}")
        arg /= 1000.0
    print(f"{arg:6.2f}B")
except TypeError:
    print(arg)
