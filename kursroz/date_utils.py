from datetime import timedelta

def day_before(date):
    return date-timedelta(days=1)

def date_str(date):
    return date.strftime("%Y/%m/%d")

def date_report_str(date):
    return date.strftime("%Y-%m-%d")
