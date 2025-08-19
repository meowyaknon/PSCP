""" 100 meter """

def main() :
    """ Check for the three fastest runner time """
    a = float(input())
    b = float(input())
    c = float(input())

    first, second, third = 1, 2, 3

    if a > b :
        a, b = b, a
        first, second = second, first
    if b > c :
        b, c = c, b
        second, third = third, second
    if a > b :
        a, b = b, a
        first, second = second, first

    test1, test2 ,test3 = a, b, c

    for i in range(4 ,9) :
        x = float(input())
        if x < test1 :
            first, second, third = i, first, second
            test1, test2 ,test3 = x, test1, test2
        elif x < test2 :
            second, third = i, second
            test2, test3 = x, test2
        elif x < test3 :
            third = i
            test3 = x
    print(first, second, third)
main()
