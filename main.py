from tests import run_voltage_test, run_current_test, run_resistance_test
from datetime import datetime
from pathlib import Path
from analysis import calculate_statistics
from report import generate_report
from config import TEST_CONFIG
from hardware import ArduinoReader

def main():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    run_directory = Path("results") / timestamp
    run_directory.mkdir(parents=True, exist_ok=True)

    print("===============================")
    print("   Automated Test System")
    print("===============================")
    print()

    USE_HARDWARE = True

    try:
        if USE_HARDWARE:
            reader = ArduinoReader(port="COM3")
            reader.connect()

            voltage_measurements = reader.collect_voltage_samples(TEST_CONFIG["voltage"]["samples"])

            voltage_passed, voltage_measurements = run_voltage_test(run_directory, measurements=voltage_measurements)
        
        else:
            voltage_passed, voltage_measurements = run_voltage_test(run_directory)

    finally:
        if reader is not None:
            reader.disconnect()


    print()
    print("----------------------------")
    print()

    current_passed, current_stats = run_current_test(run_directory)


    print()
    print("----------------------------")
    print()

    generate_report(
        run_directory / "report.txt",
        timestamp,
        voltage_measurements,
        voltage_passed,
        current_stats,
        current_passed
    )

if __name__ == "__main__":
    main()