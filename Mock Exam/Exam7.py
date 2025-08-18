""" Real """

def number() :
    """ Change the input into number """
    a = input().lower().strip()
    b = input().lower().strip()
    c = input().lower().strip()
    d = input().lower().strip()
    e = input().lower().strip()
    f = input().lower().strip()
    g = input().lower().strip()
    dp = input().lower().strip()

    if a == "on" and b == "on" and c == "on" and d == "on" \
    and e == "on" and f == "on" and g == "off" :
        num = "0"
    elif a == "off" and b == "on" and c == "on" and d == "off" \
    and e == "off" and f == "off" and g == "off" :
        num = "1"
    elif a == "on" and b == "on" and c == "off" and d == "on" \
    and e == "on" and f == "off" and g == "on" :
        num = "2"
    elif a == "on" and b == "on" and c == "on" and d == "on" \
    and e == "off" and f == "off" and g == "on" :
        num = "3"
    elif a == "off" and b == "on" and c == "on" and d == "off" \
    and e == "off" and f == "on" and g == "on" :
        num = "4"
    elif a == "on" and b == "off" and c == "on" and d == "on" \
    and e == "off" and f == "on" and g == "on" :
        num = "5"
    elif a == "on" and b == "off" and c == "on" and d == "on" \
    and e == "on" and f == "on" and g == "on" :
        num = "6"
    elif a == "on" and b == "on" and c == "on" and d == "off" \
    and e == "off" and f == "off" and g == "off" :
        num = "7"
    elif a == "on" and b == "on" and c == "on" and d == "on" \
    and e == "on" and f == "on" and g == "on" :
        num = "8"
    elif a == "on" and b == "on" and c == "on" and d == "on" \
    and e == "off" and f == "on" and g == "on" :
        num = "9"
    else :
        return "Error", dp

    return num, dp

first, dp1 = number()
second, dp2 = number()
third, dp3 = number()

if first == "Error" or second == "Error" or third == "Error" :
    print("Error")
else :
    ans = ""
    if dp1 == "on" and dp2 == "off" and dp3 == "off" :
        ans = first + "." + second + third
    elif dp1 == "off" and dp2 == "on" and dp3 == "off":
        ans = first + second + "." + third
    elif dp1 == "off" and dp2 == "off" and dp3 == "on":
        ans = first + second + third + "."
    elif dp1 == "off" and dp2 == "off" and dp3 == "off":
        ans = first + second + third
    else :
        print("Error")

    if ans != "" :
        print(f"{float(ans):.2f}")
