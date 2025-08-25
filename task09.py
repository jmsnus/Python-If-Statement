a = int(input("1-tomon: "))
b = int(input("2-tomon: "))
c = int(input("3-tomon: "))

if a == b and b == c:
    print("Teng tomonli")
    if a == b or b == c or a == c:
        print("Teng yonli")
    else:
        print("Turli tomonli")
