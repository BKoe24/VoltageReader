import matplotlib.pyplot as plt
def plot_measurements(measurements, lower_limit, upper_limit, filename):


    samples = range(1, len(measurements) + 1)

    plt.figure(figsize=(10,5))

    plt.plot(samples, measurements, label="Measured Voltage")

    plt.axhline(upper_limit, linestyle="--", label="Upper Limit")

    plt.axhline(lower_limit, linestyle="--", label="Lower Limit")

    plt.xlabel("Sample")
    plt.ylabel("Voltage (V)")
    plt.title("Voltage Test Results")

    plt.legend()
    plt.grid()

    plt.tight_layout()

    plt.savefig(filename)
