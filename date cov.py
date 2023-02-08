class DateFormat1:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class DateFormat2:
    def __init__(self, date_string):
        self.date_string = date_string


def convert_to_date_format2(date_format1):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    day = str(date_format1.day)
    month = months[date_format1.month - 1]
    year = str(date_format1.year)
    if 4 <= int(day) <= 20 or 24 <= int(day) <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][int(day) % 10 - 1]
    date_string = day + suffix + " " + month + " " + year
    return DateFormat2(date_string)
