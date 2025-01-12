def ParseRecords(input):
    reports = list()
    for line in input:
        numbers = list()
        currentNumber = str()

        for character in line:
            if character == " " or character == "\n":
                numbers.append(int(currentNumber))
                currentNumber = str()
                continue

            currentNumber += character
        reports.append(numbers)
    return reports

def CheckSafetyScore(report):
    score = int()
    increasing = None
    for i, level in enumerate(report):
        if i == 0:
            continue

        previousLevel = report[i - 1]
        currentLevel = report[i]

        score = currentLevel - previousLevel
        if score < -3 or score > 3 or score == 0:
            return False
        if increasing == True and score < 0:
            return False
        if increasing == False and score > 0:
            return False
        
        if score < 0:
            increasing = False
        else: increasing = True
        
    return True

reports = ParseRecords(open("rednose.txt"))

safeReportCount = 0
for report in reports:
    if CheckSafetyScore(report) == True:
        safeReportCount += 1
        print(report) 
    else: # Part 2
        for i, level in enumerate(report):
            reportCopy = report.copy()
            reportCopy.pop(i)
            if CheckSafetyScore(reportCopy) == True:
                safeReportCount += 1
                print(reportCopy)
                break

print(safeReportCount)