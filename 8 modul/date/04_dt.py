from datetime import datetime


month_name= {
    5: "January"
}


def day_of_week(date:str):
    d=datetime.strptime(date, "%A/%m/%Y")
    month_name[d.day]
    
    day=d.strftime ("%B")
    
    print (day)
    
    
day_of_week ("31/05/2004")