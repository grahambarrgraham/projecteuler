# https://projecteuler.net/problem=19


month_days = [('Jan', 31), ('Feb', 28), ('Mar', 31),
              ('Apr', 30), ('May', 31), ('Jun', 30),
              ('Jul', 31), ('Aug', 31), ('Sep', 30),
              ('Oct', 31), ('Nov', 30), ('Dec', 31)]


def fill_months_to(year, month, months_):
    current_month, current_year, current_weekday = months_[-1]
    current_month_days = next(i for i, v in enumerate(month_days) if current_month == v[0])
    while current_year < year or current_month != month:
        century = current_year % 100 == 0
        four_century = current_year % 400 == 0
        leap_year = True if four_century else False if century else current_year % 4 == 0
        days_in_month = 29 if current_month == 'Feb' and leap_year else month_days[current_month_days][1]
        current_weekday = (current_weekday + days_in_month) % 7
        current_month_days = (current_month_days + 1) % 12
        current_year = current_year if current_month != 'Dec' else current_year + 1
        current_month = month_days[current_month_days][0]
        months_.append((current_month, current_year, current_weekday))
    return months_


def count_sundays(from_year, to_year, to_month, months_):
    all_months = fill_months_to(to_year, to_month, months_)
    return len([_ for _, year, day_of_week in all_months if day_of_week == 0 and year >= from_year])


print(count_sundays(1901, 2000, 'Dec', [('Jan', 1900, 1)]))
