raqam = input("Telefon raqamini kiriting: ")
kod = raqam[:2]

if kod == "90" or kod == "91":
    print("Ucell")
else:
    if kod == "93" or kod == "94":
        print("Beeline")
    else:
        if kod == "95" or kod == "97":
            print("Uzmobile")
        else:
            if kod == "88" or kod == "99":
                print("Mobiuz")
            else:
                print("Noma’lum operator")
