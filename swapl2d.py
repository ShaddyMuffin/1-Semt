n = int(input())
if n>9:
    first= n%10
    both = n%100
    second = both//10
    n -= both
    both = (first*10)+second
    n+=both
    print(n)
else:
    print("Larger number!")