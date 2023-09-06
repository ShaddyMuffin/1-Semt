age = int(input())

if age>=18:
    print("Vote for a better future!")
else:
    if 0<age<18:
        print("Vote in",18-age,"years!")
    else:
        print("Error!")