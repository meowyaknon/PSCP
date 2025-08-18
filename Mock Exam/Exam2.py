""" Digital Wallet """

name = input()
thai = input().upper()
house = input().upper()
age = float(input())
income = float(input())
bank = float(input())

if thai == "YES" or thai == "TRUE" :
    if house == "YES" or house == "TRUE" :
        if age >= 16 :
            if bank <= 500000 :
                if income <= 840000 :
                    print(f"Congratulations! {name} is qualified to receive a digital wallet \
amount of 10,000 baht, sponsored by all taxpayers in Thai and.")
                else :
                    print(f"Unfortunately, {name} is not qualified.")
            else :
                print(f"Unfortunately, {name} is not qualified.")
        else :
            print(f"Unfortunately, {name} is not qualified.")
    else :
        print(f"Unfortunately, {name} is not qualified.")
else :
    print(f"Unfortunately, {name} is not qualified.")
