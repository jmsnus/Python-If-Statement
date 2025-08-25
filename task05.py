pul = int(input("omonat summasini kiriting: "))

if pul < 100000:
    print("5%")
else:
    if pul <= 500000:
        print("7%")
    else:
        print("10%")
