import time
start = time.time()
num = int(input())
for i in range(2, num//2):
    if(num % i == 0):
        print("flase");
        break
    else:
        print("true")
end = time.time()
print(end - start)