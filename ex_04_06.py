def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40 :
        # print("Overtime")
        reg = rate * hours
        opt = (hours - 40.0) * (rate * 0.5)
        # print(reg,opt)
        pay = reg + opt
    else:
        # print("Regular")
        pay = hours * rate
    # print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
xp = computepay(fh, fr)
print("Pay:",xp)


# fr ex_03_01
