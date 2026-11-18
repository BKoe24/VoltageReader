def generate_report(
        filename,
        test_id,
        voltage_stats,
        voltage_passed,
        current_stats,
        current_passed
):
    with open(filename, "w") as file:

        file.write("============================================\n")
        file.write("               Test Report\n")
        file.write("============================================\n")

        file.write(f"Test ID: {test_id}\n\n")

        file.write(f"--------------------------------------------\n")
        file.write("VOLTAGE TEST\n")
        file.write(f"--------------------------------------------\n")

        file.write(f"Minimum: {voltage_stats[1]:.3f} V\n")
        file.write(f"Maximum: {voltage_stats[2]:.3f} V\n")
        file.write(f"Average: {voltage_stats[0]:.3f} V\n")

        if voltage_passed:
            file.write("RESULT: PASS\n")
        else:
            file.write("RESULT: FAIL\n")


        file.write(f"--------------------------------------------\n")
        file.write("CURRENT TEST\n")
        file.write(f"--------------------------------------------\n")

        file.write(f"Minimum: {current_stats[1]:.3f} A\n")
        file.write(f"Maximum: {current_stats[2]:.3f} A\n")
        file.write(f"Average: {current_stats[0]:.3f} A\n")

        if current_passed:
            file.write("RESULT: PASS\n")
        else:
            file.write("RESULT: FAIL\n")

        file.write("\n")

        file.write("============================================\n")

        if voltage_passed and current_passed:
            file.write("FINAL RESULT: PASS\n")
        else:
            file.write("FINAL RESULT: FAIL\n")

        file.write("============================================\n")