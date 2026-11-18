from config import TEST_CONFIG
from data import collect_voltage_samples, collect_current_samples
from analysis import calculate_statistics, check_limits
from plotting import plot_measurements
from results import save_measurements


def run_voltage_test(run_directory, measurements=None):
   

    voltage_config = TEST_CONFIG["voltage"]

    if measurements is None:
        print("Starting simulated voltage test...")
        print()
        measurements = collect_voltage_samples(voltage_config["samples"])

    average, minimum, maximum = calculate_statistics(measurements)

    passed = check_limits(measurements, voltage_config["min"], voltage_config["max"])

    print("Voltage Test Results")
    print("--------------------")
    print(f"Samples: {len(measurements)}")
    print(f"Average: {average:.3f} V")
    print(f"Minimum {minimum:.3f} V")
    print(f"Maximum: {maximum:.3f} V")

    if passed:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    plot_measurements(measurements, voltage_config["min"], voltage_config["max"], run_directory / "VoltageGraph")
    save_measurements(run_directory / "VoltageTest.csv", measurements)

    return passed, [average,minimum,maximum]

def run_current_test(run_directory):

    print("Starting simulated current test...")
    print()

    current_config = TEST_CONFIG["current"]

    measurements = collect_current_samples(current_config["samples"])

    average, minimum, maximum = calculate_statistics(measurements)

    passed = check_limits(measurements, current_config["min"], current_config["max"])

    print("Current Test Results")
    print("--------------------")
    print(f"Samples: {len(measurements)}")
    print(f"Average: {average:.3f} A")
    print(f"Minimum {minimum:.3f} A")
    print(f"Maximum: {maximum:.3f} A")

    if passed:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")

    plot_measurements(measurements, current_config["min"], current_config["max"], run_directory / "CurrentGraph")
    save_measurements(run_directory / "CurrentTest.csv", measurements)

    return passed, [average,minimum,maximum]

def run_resistance_test(run_directory, measurements):

    resistance_config = TEST_CONFIG["resistance"]

    plot_measurements(measurements, resistance_config["min"], resistance_config["max"], run_directory / "ResistanceGraph")
    save_measurements(run_directory / "ResistanceTest.csv", measurements)
