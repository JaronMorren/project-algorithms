def study_schedule(permanence_period, target_time):
    # Initializes a counter variable that starts from zero
    #  to keep track of the number of periods
    #  that include the target_time
    period_counter = 0

    try:
        # Iterates over each period in permanence_period
        for period in permanence_period:
            # Checks if the target_time falls within the current period
            if period[0] <= target_time <= period[1]:
                # If the target_time is within the beginning period
                #  and the ending period, the period_counter increments by 1
                period_counter += 1
    except TypeError:
        # If a TypeError occurs
        # (for example permanence_period is not iterable),
        #  return None
        return None
# Return the final count of periods that includes the target_time
    return period_counter
