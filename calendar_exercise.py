from datetime import datetime, timedelta


def calendar_availability(calendar1, calendar2, disponility1, disponility2, delta_minutes):
    booked_times = []
    calendar1_len = len(calendar1)
    calendar2_len = len(calendar2)
    i, j = 0, 0
    # fill all booked times list
    while i < calendar1_len and j < calendar2_len:
        calendar1_initial, calendar1_final = calendar1[i]
        calendar2_initial, calendar2_final = calendar2[j]

        if compare_times(calendar1_initial, calendar2_initial) < 0:
            booked_times.append(calendar1[i])
            i += 1
        elif compare_times(calendar1_initial, calendar2_initial) == 0:
            if compare_times(calendar1_final, calendar2_final) < 0:
                booked_times.append(calendar1[i])
                booked_times.append(calendar2[j])
                i += 1
                j += 1
            else:
                booked_times.append(calendar2[j])
                booked_times.append(calendar1[i])
                j += 1
                i += 1
        else:
            booked_times.append(calendar2[j])
            j += 1

    if i < calendar1_len:
        booked_times.extend(calendar1[i:])
    elif j < calendar2_len:
        booked_times.extend(calendar2[j:])

    # calculate disponibility range of the 2 calendars
    disponibility = []
    disponibility.append(disponility1[0] if compare_times(
        disponility1[0], disponibility2[0]) > 0 else disponility2[0])
    disponibility.append(disponility1[1] if compare_times(
        disponility1[1], disponility2[1]) < 0 else disponility2[1])

    # A calendar with contigous hours joined by a single hour
    calendar = mix_times(booked_times)

    return calculate_availability(calendar, disponibility, delta_minutes)


def compare_times(time1, time2, timedelta1=0, timedelta2=0):
    time1 = datetime.strptime(time1, '%H:%M') + timedelta(minutes=timedelta1)
    time2 = datetime.strptime(time2, '%H:%M') + timedelta(minutes=timedelta2)
    if time1 > time2:
        return 1
    if time1 == time2:
        return 0
    return -1


def mix_times(booked_times):
    i, j = 0, 0
    while i < len(booked_times) and j < len(booked_times):
        j = i + 1
        start_time, end_time = booked_times[i]
        start_time_2, end_time_2 = booked_times[j]

        if compare_times(end_time, start_time_2) >= 0 and compare_times(end_time, end_time_2) <= 0:
            booked_times[i] = ([start_time, end_time_2])
            booked_times.pop(j)
        elif compare_times(end_time, start_time_2) < 0:
            i += 1
        elif compare_times(end_time, end_time_2) > 0:
            booked_times.pop(j)
    return booked_times


def calculate_availability(calendar, disponibility, delta_minutes):
    availability = []
    disponibility_initial = disponibility[0]
    disponibility_final = disponibility[1]

    for i in range(len(calendar)):
        calendar_hour_initial, calendar_hour_final = calendar[i]

        if compare_times(disponibility_initial, calendar_hour_initial) > 0:
            calendar_hour_initial = disponibility_initial

        elif compare_times(disponibility_final, calendar_hour_final) < 0:
            calendar_hour_final = disponibility_final

        if i == 0:
            if (compare_times(disponibility_initial, calendar_hour_initial) < 0 and
                    compare_times(disponibility_initial, calendar_hour_initial, delta_minutes) <= 0):
                availability.append(
                    [disponibility_initial, calendar_hour_initial])
        elif i == len(calendar) - 1:
            if (compare_times(disponibility_final, calendar_hour_final) > 0 and
                    compare_times(disponibility_final, calendar_hour_final, 0, delta_minutes) >= 0):
                availability.append([calendar_hour_final, disponibility_final])
                break

        calendar_hour2_initial, calendar_hour2_final = calendar[i + 1]

        if(compare_times(calendar_hour_final, calendar_hour2_final, delta_minutes) <= 0):
            availability.append([calendar_hour_final, calendar_hour2_initial])

    return availability


if __name__ == '__main__':
    calendar1 = [('09:00', '10:30'), ('10:00', '10:30'),
                 ('12:00', '13:00'), ('16:00', '18:00')]
    calendar2 = [('10:00', '11:30'), ('12:30', '14:30'),
                 ('14:30', '15:00'), ('16:00', '17:00')]

    disponibility1 = ['08:00', '20:00']
    disponibility2 = ['08:30', '19:00']

    delta_time = 30

    print(calendar_availability(calendar1, calendar2,
                                disponibility1, disponibility2, delta_time))
