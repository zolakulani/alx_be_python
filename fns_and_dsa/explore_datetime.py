import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current date and time: {current_date}')

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    timedelta = datetime.timedelta(days=number_of_days)
    current_date = datetime.datetime.now()
    future_date = current_date + timedelta 
    future_date = future_date.strftime("%Y-%m-%d")
    print(f'Future date: {future_date}')

display_current_datetime()
calculate_future_date()