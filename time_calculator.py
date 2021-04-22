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
        (str): The time the duration ends.
    """
    start_hr, _s = start.split(":")
    start_min, period = _s.split(" ")
    duration_hr, duration_min = duration.split(":")

    # str => int
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
    # Count days
    num_days = end_hr // 24
    # Final hour is within 24 HRs
    end_hr = end_hr % 24

    # Formatting the return string.
    # AM / PM
    # 00:00 - 11:59HR is AM
    if end_hr < 12:
        p = "AM"
        # 00:00 midnight is 12:00 AM
        if end_hr == 0:
            end_hr = 12
    # 13:00 - 23:59HR is PM
    elif end_hr > 12:
        p = "PM"
        end_hr -= 12
    # 12:00 noon is PM
    elif end_hr == 12:
        p = "PM"
        end_hr = 12
    # "0" padding for minutes < 10
    if end_min < 10:
        min = "0" + str(end_min)
    else:
        min = str(end_min)
    hr = str(end_hr)

    result = hr + ":" + min + " " + p
    if not day:
        # Same day
        if num_days == 0:
            return result

        # The next day
        elif num_days == 1:
            return result + " (next day)"

        # `n` days later
        else:
            return result + " (" + str(num_days) + " days later)"

    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    final_day = None
    for k, d in days.items():
        if d == day.capitalize():
            final_day = days[(k + num_days) % 7]

    result += ", " + final_day
    # Same day
    if num_days == 0:
        return result
    # The next day
    elif num_days == 1:
        return result + " (next day)"
    # `n` days later
    else:
        return result + " (" + str(num_days) + " days later)"
