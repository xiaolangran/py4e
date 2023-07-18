score = input("Enter Score:")
fs = float(score)
if fs > 1.0 or fs < 0:
    print("An error! Out of range.")
elif fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
elif 0 < fs < 0.6:
    print("F")
