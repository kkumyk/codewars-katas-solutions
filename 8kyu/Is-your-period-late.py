from datetime import date

def period_is_late(last,today,cycle_length):
    delta = today - last
    return delta.days > cycle_length

period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35)