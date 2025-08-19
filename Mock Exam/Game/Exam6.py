""" Game """

def main() :
    """ Find the lowest amount can draw happen """
    a = int(input())
    b = int(input())

    draw_count = b % 3

    if a % 3 == b % 3 :
        print(draw_count)
    else :
        print("Error")
main()
