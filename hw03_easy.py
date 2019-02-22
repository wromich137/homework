
a = 2.1234567
b = 2.9999967
c = 2.1999967
def my_round(a,n):
    x = str(a)
    p = "0."+"0"*(n-3)+"1" #добавляю единицу, которую нужно будет добавить к последнему разряду
    if int(x[n:n+1]) >= 5:
        l = float(x[:n])+float(p)
    else:
        l = x[:n]
    return l

print(my_round(a,3))
print(my_round(b,3))
print(my_round(c,3))

ticket1 = "160230"
ticket2 = "160070"
num1 = 0
num2 = 0

def lucky_ticket(ticket1):
    num1 = 0
    num2 = 0
    for number in ticket1[:3]:
        num1 += int(number)

    for number in ticket1[3:]:
        num2 += int(number)

    if num1 == num2:
        return "Lucky"
    else:
        return "Not lucky"

print(lucky_ticket(ticket1))