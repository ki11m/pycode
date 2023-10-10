num = int(input())
for i in range(2, num//2):
    if(num % i == 0):
        print("flase");
        break
    else:
        print("true")