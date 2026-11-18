import random

def collect_voltage_samples(num_samples):
    measurements = []

    for i in range(num_samples):
        voltage = random.gauss(5.0,0.05)
        measurements.append(voltage)

    return measurements

def get_current():
    """Simmulate a current measurement"""
    return random.gauss(0.5,0.02)

def collect_current_samples(num_samples):

    measurements = []

    for i in range(num_samples):
        current = get_current()
        measurements.append(current)

    return measurements