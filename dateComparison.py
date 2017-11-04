
daysofMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##################Leaf year function#########################################################

def userInput():
    global startDate, startYear, startMonth, endMonth, endYear, endDate

    startDate = input("Please enter start Date(MM/DD/YYYY):")
    endDate = input("Please enter end Date(MM/DD/YYYY):")
    ###################splid date month and year################################################
    startDateList = startDate.split("/")
    endDateList = endDate.split("/")
    startYear = int(startDateList[2])
    endYear = int(endDateList[2])
    startDate = int(startDateList[1])
    endDate = int(endDateList[1])
    startMonth = int(startDateList[0])
    endMonth = int(endDateList[0])

    finalDaysdifference(startDate, endDate, startYear, endYear, startMonth, endMonth)


def LeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



###########################days calcultion for month###############################
def DaysforMonths(month, year):
    days = 0
    monthindex = 0
    for monthindex in range(0, int(month-1)):
        if monthindex == 1:
            if LeapYear(year) == True:
                days = days + 29
            else:
                days = days + 28
        else:
            days = days + daysofMonths[monthindex]
       # print(days)
    return days

def DaysforeachMonths(month, year):
    days = 0
    monthindex = 0
    for monthindex in range(int(month-1), 12):
        if monthindex == 1:
            if LeapYear(year) == True:
                days = days + 29
            else:
                days = days + 28
        else:
            days = days + daysofMonths[monthindex]
       # print(days)
    return days



#################################days calulation for year

def noOfDaysBasedYears(startYear,endYear):
    noOfdaysBetweenYears=0
    if startYear==endYear:
        if LeapYear(startYear) == True:
            noOfdaysBetweenYears = noOfdaysBetweenYears + 366
        else:
            noOfdaysBetweenYears = noOfdaysBetweenYears + 365
        print(noOfdaysBetweenYears)
        return noOfdaysBetweenYears
    else:
        for years in range(int(startYear),int(endYear)):
            if LeapYear(years)==True:
                noOfdaysBetweenYears=noOfdaysBetweenYears+366
            else:
                noOfdaysBetweenYears=noOfdaysBetweenYears+365
    #print(noOfdaysBetweenYears)
    return noOfdaysBetweenYears



def finalDaysdifference(startdate,endDate,startYear,endYear,startMonth,endMonth):

    noOfdays = 0
    if startYear==endYear:
     finalNoOfDays=noOfDaysBasedYears(startYear,endYear)-DaysforMonths(startMonth,startYear)-int(startdate)-DaysforeachMonths(endMonth,endYear)+int(endDate)
    else:

     finalNoOfDays = noOfDaysBasedYears(startYear, endYear) - DaysforMonths(startMonth, startYear) - int(startdate) + DaysforMonths(endMonth, endYear) + int(endDate)

    print("No of days between two dates:",finalNoOfDays)


if __name__ == '__main__':
 userInput()











