import spidev
import time

class MCP4162:
    def __init__(self, bus=0, device=0, max_speed_hz=500000):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz

    def write_pot(self, value):
        command_byte = 0x00  # Command byte for writing to wiper 0
        data_byte = value & 0xFF  # Ensure the value is 8-bit
        self.spi.xfer([command_byte, data_byte])

    def sweep(self, sweep_range=128, delay=0.01):
        # Increase potentiometer value
        for i in range(sweep_range):
            self.write_pot(i)
            time.sleep(delay)

        # Decrease potentiometer value
        for i in range(sweep_range - 1, -1, -1):
            self.write_pot(i)
            time.sleep(delay)

    def close(self):
        self.spi.close()

# Usage example
try:
    potentiometer = MCP4162()
    while True:
        potentiometer.sweep()
except KeyboardInterrupt:
    potentiometer.close()
