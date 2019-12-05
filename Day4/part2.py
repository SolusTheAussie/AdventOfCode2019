count = 0
for n in range(357253, 892942+1):
    numberList = str(n) + "a"
    satisfied = False

    lastLastLastDigit = "!"
    lastLastDigit = "!"
    lastDigit = " "
    for digit in numberList:
        if lastDigit == lastLastDigit and lastDigit != digit and lastLastDigit != lastLastLastDigit:
            satisfied = True
        if digit < lastDigit:
            satisfied = False
            break
        lastLastLastDigit = lastLastDigit
        lastLastDigit = lastDigit
        lastDigit = digit

    if satisfied:
        count += 1

print(count)