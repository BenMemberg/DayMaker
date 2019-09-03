# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

## Function definitions

# Main function (called when "python DayMaker.py" is run)
def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [0] * 96

    ## TESTS ##
    # print(indexConvert(50))
    # print(timeConvert('12:30'))
    # scheduleEvent('17:35', '18:55', 1, dayList)
    # print(dayList)


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

# Calls the main function
if __name__== "__main__" : 
    main()