from datetime import date


def get_days_in_month(month, year):
    if year % 2 == 0:
        leap_year = True
    else:
        leap_year = False

    days_in_month = {
        1:31,
        2:29 if leap_year else 28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    if month<1 or month > 12:
            return "wrong month"
    return get_days_in_month [month]