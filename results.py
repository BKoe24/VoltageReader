import csv

def save_measurements(filename, measurements):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Sample","Voltage"])

        for number, voltage in enumerate(measurements,start=1):
            writer.writerow([number,voltage])