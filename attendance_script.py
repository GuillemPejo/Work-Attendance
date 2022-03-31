import datetime, csv, random

def getRandomBetween(start, end):
    return str(random.randint(start,end))

def main():
    now = datetime.datetime.now()

    START_HOUR= "08" #Time you start working 
    LEAVE_HOUR = "17" #Time you finish working 
    HOLIDAYS = [] #Days you've been on vacation, example: [1, 5, 18] 

    ID = "877" #Self user ERP id
    EMPLOYE_ID = "__export__.hr_employee_" + ID

    ACTION_ENTER = "Registrar entrada"
    ACTION_LEAVE = "Registrar salida"

    FILENAME = "attendance_" + now.strftime("%B") + str(now.year) + ".csv"
    CSV_HEADER = ["employee_id/id",'name','action']

    daysNotWorked = []
    
    for day in HOLIDAYS:
        daysNotWorked.append(datetime.date(now.year, now.month, day))

    csvRows = []
    
    for i in range(1, 32):
        try:
            thisdate = datetime.date(now.year, now.month, i)
        except(ValueError):
            break
        if thisdate.weekday() < 5 and thisdate not in daysNotWorked:
            businessDaysData = []
            businessDaysData.append(EMPLOYE_ID)
            businessDaysData.append(str(thisdate) + " " + START_HOUR +":"+getRandomBetween(0,3) + getRandomBetween(0,9) + ":00")
            businessDaysData.append(ACTION_ENTER)
            csvRows.append(businessDaysData)
            businessDaysData = []
            businessDaysData.append(EMPLOYE_ID)
            businessDaysData.append(str(thisdate) + " " + LEAVE_HOUR +":"+ getRandomBetween(0,5) + getRandomBetween(0,9) + ":00")
            businessDaysData.append(ACTION_LEAVE)
            csvRows.append(businessDaysData)

    with open(FILENAME, 'w') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(CSV_HEADER)
        for row in csvRows:
            writer.writerow(row)
        
if __name__ == '__main__':
    main()
