import time
import serial

class ArduinoReader:
    """Read voltage measurements form an Arduino over USB"""

    def __init__(self, port, baud_rate=9600, timeout=2):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.connection = None

    def connect(self):
        """Open the serial connection to the Arduino"""
        self.connection = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)

        #Give time for arduino to reset
        time.sleep(2)

        #Get rid of startup data
        self.connection.reset_input_buffer()

        print(f"Connected to Arduino on {self.port}")

    def read_voltage(self):
        """Read a voltage measurement"""
        if self.connection is None or not self.connection.is_open:
            raise RuntimeError("Arduino is not connected")

        line = self.connection.readline().decode("utf-8").strip()

        if not line:
            raise TimeoutError("No data recieved from Arduino")

        try:
            voltage = float(line)
        except ValueError as error:
            raise ValueError(f"Invalid voltage data received: {line!r}") from error

        return voltage

    def collect_voltage_samples(self, num_samples):
        """Collect a fixed number of voltage measurements"""
        if num_samples <= 0:
            raise ValueError("num_samples must be positive")

        print("Starting hardware voltage test")
        measurements = []
        for _ in range(num_samples):
            voltage = self.read_voltage()
            measurements.append(voltage)
            #print(f"Measured: {voltage:.3f} V")

        return measurements


    def read_value(self):
        """Read a measurement"""
        if self.connection is None or not self.connection.is_open:
            raise RuntimeError("Arduino is not connected")

        line = self.connection.readline().decode("utf-8").strip()

        if not line:
            raise TimeoutError("No data recieved from Arduino")

        try:
            value = float(line)
        except ValueError as error:
            raise ValueError(f"Invalid data received: {line!r}") from error

        return value

    def collect_samples(self, num_samples):
            """Collect a fixed number of measurements"""
            if num_samples <= 0:
                raise ValueError("num_samples must be positive")
    
            print("Starting hardware test")
            measurements = []
            for _ in range(num_samples):
                voltage = self.read_voltage()
                measurements.append(voltage)
                #print(f"Measured: {:.3f} ")
    
            return measurements

    def disconnect(self):
        """Close the serial connection safely"""
        if self.connection is not None and self.connection.is_open:
            self.connection.close()
            print("Arduino connection is closed.")

        self.connection = None