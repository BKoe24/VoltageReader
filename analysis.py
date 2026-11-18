def calculate_statistics(measurements):
    average = sum(measurements) / len(measurements)
    minimum = min(measurements)
    maximum = max(measurements)

    return average, minimum, maximum


def check_limits(measurements, lower_limit, upper_limit):
    for measurement in measurements:
        if measurement < lower_limit:
            return False

        if measurement > upper_limit:
            return False

    return True