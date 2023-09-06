X = int(input("Available seats : "))
Y = int(input("Curious Students : "))
if X==Y:
    print("Everyone gets seat!")
elif X>Y:
    print("More than enogh")
else:
    print("{} extra seats are needed".format(Y-X))