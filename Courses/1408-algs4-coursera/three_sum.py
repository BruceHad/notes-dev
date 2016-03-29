import time, random

def ThreeSum(numbers):
    length = len(a)
    count = 0
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if(numbers[i] + numbers[j] + numbers[k] == 0):
                    count+=1
    return count

def generateInts(n):
    ints = []
    for i in range(n):
        ints.append(random.randint(-999, 999))
    return ints

if __name__ == "__main__":
    for i in range(10, 250, 10):
        a = generateInts(i)
        start_time = time.time()
        count = ThreeSum(a)
        end_time = time.time()
        print(i, count, end_time - start_time)
