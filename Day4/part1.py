count = 0
for n in range(357253, 892942+1):
    numberList = str(n)
    satisfied = False

    lastDigit = " "
    for digit in numberList:
        if digit == lastDigit:
            satisfied = True
        if digit < lastDigit:
            satisfied = False
            break
        lastDigit = digit

    if satisfied:
        count += 1

print(count)