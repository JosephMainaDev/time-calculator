def add_time(start, duration, day = None):
    """
    Adds `duration time` to `start time` and returns the result.

    This function uses the 24 HR system. I prefer it because it is easier
    to think about.

    Arguments:
        start (str): Time in the 12-hour clock format (with AM or PM).
        duration (str): Time in hours and minutes.
        day (str, optional): A starting day of the week.

    Returns:
        new_time (str): The time the duration ends.
    """
    new_time = ""

    start_hr, _s = start.split(":")
    start_min, period = _s.split(" ")
    duration_hr, duration_min = duration.split(":")

    # I prefer using the 24 HR system.
    # Add 12 hours to `start_hr` if it is past noon.

    end_hr = int(start_hr) + int(duration_hr)
    end_min = int(start_min) + int(duration_min)

    # Increment hours if min > 59
    end_hr += end_min // 60

    # Minutes have a max val of 59
    end_min = end_min % 60

    return new_time

# add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")