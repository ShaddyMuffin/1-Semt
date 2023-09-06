PMax = int(input("Max marks in PHYSICS: "))
CMax = int(input("Max marks in CHEMISTRY: "))
MMax = int(input("Max marks in MATH: "))

p = int(input("Your marks in PHYSICS: "))
c = int(input("Your marks in CHEMISTRY: "))
m = int(input("Your marks in MATHS: "))

cutoff = (PMax/4)+(CMax/4)+(MMax/2)

totalmarks=p+c+m

if totalmarks<=cutoff:
    print("4 years of pure joy. :)")
else:
    print("Life saved")