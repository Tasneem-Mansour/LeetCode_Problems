class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def isLeapYear(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

            # leapYear = 0
            # if year == 300 or 700 or  1900 or 2000:
            #     if year % 400 == 0:
            #         leapYear = 1
            # else: 
            #     if year % 4 == 0:
            #         leapYear = 1

            # return leapYear

        def daysInMonth(year, month) -> int:
            days = [31, 28 + int(isLeapYear(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            return days[month-1]



        def calculateDays(date):
            #date = "1983-04-05"
            date  = date.split("-")
            year  = int(date[0])
            month = int(date[1])
            day   = int(date[2])

            days = 0

            for y in range(1971, year):
                days += 365 + int(isLeapYear(y))

            for m in range(1, month):
                days += daysInMonth(year, m)            #for jan to nov 

            days += day                                 #count days in dec
            return days

        return abs(calculateDays(date1)-calculateDays(date2))


        
        