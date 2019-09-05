# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

## Function definitions

# Main function (called when "python DayMaker.py" is run)
def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [-1] * 96

    runTests(dayList)

def scheduleBounds(start, finish, dayList):
        dayList[timeConvert(start)] = 0
        dayList[timeConvert(finish)] = -2


# Given an index in the List, converts it to properly formatted military time
def indexConvert(i):
    return str(int(i/4)) + ':' + str(i%4*15).zfill(2)

# Given properly formatted military time string, converts it to an index in the dayList
def timeConvert(time):
    t = time.split(':')
    return int(int(t[0])*4 + int(t[1])/15)

# Adds an event id to dayList based on time
def scheduleEvent(start, stop, id, dayList):
    r = range(timeConvert(start), timeConvert(stop))
    for i in r:
        dayList[i] = id

# Test function
def runTests(dayList):
    
    ## TESTS ##
    scheduleBounds('17:00', '2:30', dayList)
    print(indexConvert(50))
    print(timeConvert('12:30'))
    scheduleEvent('20:00', '23:30', 1, dayList)
    for x in range(len(dayList)):
        if (dayList[x] != 1):
                print(indexConvert(x) + ' - ' + str(dayList[x]))
        else:
                print(indexConvert(x) + ' - ' + 'Your Concert!')
        

# Calls the main function
if __name__== "__main__" : 
    main()