from datetime import date, timedelta, datetime

today = date.today()
display_today = datetime.strftime(today, "%d-%m-%y")
subtract_one_day = timedelta(days=1)
subtract_two_day = timedelta(days=2)
week_back_in_time = timedelta(days=7)

yesterday = today - subtract_one_day
display_yesterday = datetime.strftime(yesterday, "%d-%m-%Y")
day_before_yesterday = today - subtract_two_day
last_week = today - week_back_in_time


if __name__ == "__main__":
    pass