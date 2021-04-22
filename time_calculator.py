def add_time(start, duration, day = None):
    """
    Adds `duration time` to `start time` and returns the result.

    This function uses the 24 HOUR system. I prefer it because it is easier
    to think about.

    Arguments:
        start (str): Time in the 12-hour clock format (with AM or PM).
        duration (str): Time in hours and minutes.
        day (str, optional): A starting day of the week.

    Returns:
        new_time (str): The time the duration ends.
    """
    start_hr, _s = start.split(":")
    start_min, period = _s.split(" ")
    duration_hr, duration_min = duration.split(":")

    # str() => int()
    start_hr = int(start_hr)
    start_min = int(start_min)
    duration_hr = int(duration_hr)
    duration_min = int(duration_min)

    # I prefer using the 24 HR system.
    # Add 12 hours to `start_hr` if it is past noon.
    if period == "PM" and start_hr != 12:
        start_hr = start_hr + 12

    # 12:00 AM midnight is 00:00 HRS.
    if period == "AM" and start_hr == 12:
        start_hr = 0

    end_hr = start_hr + duration_hr
    end_min = start_min + duration_min

    # Increment hours if min > 59
    end_hr += end_min // 60

    # Minutes have a max val of 59
    end_min = end_min % 60

    num_days = end_hr // 24
    # Final hour is within 24 HRs
    end_hr = end_hr % 24

    # return str formatting
    # "0" padding for minutes < 10
    if end_min < 10:
        min = "0" + str(end_min)
    else:
        min = str(end_min)

    # AM / PM
    if end_hr < 12:
        p = "AM"
        if end_hr == 0:
            end_hr = 12
    elif end_hr > 12:
        p = "PM"
        end_hr -= 12
    elif end_hr == 12:
        p = "PM"
        end_hr = 12

    hr = str(end_hr)

    # Tests: [1, ]
    if not day:
        # Same day
        if num_days == 0:
            return hr + ":" + min + " " + p

        elif num_days == 1:
            return hr + ":" + min + " " + p + " (next day)"

        else:
            return hr + ":" + min + " " + p + " (" + str(num_days) + " days later)"

    # Tests:[]
    final_day = ""
    if day:
        # How many days are gone?
        num_days = end_hr // 24

        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }

        for k, v in days.items():
            if v == day.capitalize():
                final_day = days[(k + num_days) % 7]

    return

# add_time("3:00 PM", "3:10")
# add_time("11:30 AM", "2:32", "Monday")
# add_time("9:15 PM", "5:30")
# add_time("12:59 PM", "24:05")
# add_time("12:59 AM", "24:05")

print(add_time("11:59 PM", "24:05"))