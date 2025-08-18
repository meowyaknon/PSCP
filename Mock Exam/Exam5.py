""" Post Office """

n = int(input())
m = int(input())

def envelop_check(weight) :
    """ Check Weight of envelop for price """
    if 0 < weight <= 10 :
        return 16
    elif 10 < weight <= 20 :
        return 18
    elif 20 < weight <= 100 :
        return 23
    elif 100 < weight <= 250 :
        return 28
    elif 250 < weight <= 500 :
        return 33
    elif 500 < weight <= 1000 :
        return 48
    elif 1000 < weight <= 2000 :
        return 68

def package_check(weight) :
    """ Check Weight of package for price """
    if 0 < weight <= 500 :
        return 45
    elif 500 < weight <= 1000 :
        return 55
    elif 1000 < weight <= 2000 :
        return 70

def main() :
    """ Calcualte Total Price """
    total = 0

    for _ in range(n) :
        envelop = float(input())
        total += envelop_check(envelop) + 13

    for _ in range(m) :
        package = float(input())
        total += package_check(package) + 15
    print(total)
main()
