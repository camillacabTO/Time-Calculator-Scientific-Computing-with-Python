def add_time(start, duration, day_of_week=None):
    [hour, minute, am_pm] = start.replace(':', ' ').split()
    [additional_hour, additional_minute] = duration.split(':')
    full_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    hour_result = int(hour) + int(additional_hour)
    minute_result = int(minute) + int(additional_minute)
    additional_days = hour_result / 24

    if minute_result >= 60:
        minute_result = minute_result % 60
        hour_result += 1

    if hour_result >= 12:
        if am_pm == 'PM':
            additional_days += 1
        if hour_result % 24 >= 12:
            am_pm = 'AM' if am_pm == 'PM' else 'PM'

        hour_result = hour_result % 12 if hour_result % 12 != 0 else 12

    if len(str(minute_result)) <= 1:
        minute_result = '0' + str(minute_result)

    if int(additional_days) == 0:
        output_days = ''
    elif int(additional_days) == 1:
        output_days = ' (next day)'
    else:
        output_days = f' ({str(int(additional_days))} days later)'

    if day_of_week is not None:
        index = full_week.index(day_of_week.lower())
        result_week_index = index + int(additional_days)

        if result_week_index > 6:
            result_weekday = full_week[result_week_index % 7].capitalize()
        else:
            result_weekday = full_week[result_week_index].capitalize()

        return f'{hour_result}:{minute_result} {am_pm}, {result_weekday}{output_days}'

    return f'{hour_result}:{minute_result} {am_pm}{output_days}'
