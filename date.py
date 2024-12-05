import datetime
def get_previous():    
    today = datetime.date.today()
    print(today)
    first = today.replace(day=1)
    print("first", first)
    last_month = first - datetime.timedelta(days=1)
    print("datetime.timedelta(days=1)", datetime.timedelta(days=1))
    second_last_month = last_month.replace(day=1) - datetime.timedelta(days=1)
    third_last_month = second_last_month.replace(day=1) - datetime.timedelta(days=1)


    third_last_month_str = third_last_month.strftime("%Y-%m")
    last_month_str = last_month.strftime("%Y-%m")
    second_last_month_str = second_last_month.strftime("%Y-%m")
    
    return last_month_str, second_last_month_str, third_last_month_str

print(get_previous())