def checkSafe(report):
    increase = False
    decrease = False
    loop = 0
    for i in range(len(report)-1):

        diff = abs(report[i] - report[i+1]) # Get the absolute difference 
        
        if diff not in [1,2,3]: # If difference is not between at least one and at most three, skip the report
            break
        
        # Assign True to the increasing/decreasing patterns
        if report[i] < report[i+1]:
            increase = True
        elif report[i] > report[i+1]:
            decrease = True
            
        if increase and decrease: # if somehow both increasing/decreasing pattern is found, skip the report
            break
        
        loop += 1
        
        # if loop runs till end without changing pattern and being in diff limits, return as safe report
        if loop == len(report)-1:
            return 1
    
    # if anything breaks, unsafe report
    return 0

# Function to check whether an report is safe when modified, recursively
def checkSafeModified(report, modification=0):
    # Since one report can tolerate only one single bad level
    if modification > 1:
        # Exit as unsafe if report has more than one bad level 
        return 0
    
    # check first if given report is safe without any modification
    if checkSafe(report):
        return 1
    
    # Build new report, each time by excluding current index(i)
    for i in range(len(report)):
        newreport = report[:i] + report[i+1:]
        # check if one removal genarates safe report
        if checkSafeModified(newreport, modification + 1):
            return 1
    return 0

totalSafe = 0
with open("day_02/input.txt", 'r') as file:
    for line in file:
        val = [int(v) for v in line.split()]
        totalSafe += checkSafeModified(val)
    
    print(f"Total number of safe reports when they are modified: {totalSafe}")