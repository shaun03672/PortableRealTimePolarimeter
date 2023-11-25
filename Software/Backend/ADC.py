import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

def read_adc():
    # Send read command and get the response
    # MAX1242/MAX1243 uses a 12-bit ADC with the MSB first
    # For these ADCs, the data is clocked on the falling edge of SCLK,
    # so we set CPHA to 0 (SPI mode 0)
    # We read two bytes from the SPI bus
    resp = spi.xfer2([0x00, 0x00])
   
    # Combine the two bytes and extract the ADC value
    # ((resp[0] & 0x0F) << 8) combines the lower 4 bits of the first byte with the second byte
    # resp[1] is the second byte and contains the lower 8 bits of the result
    value = ((resp[0] & 0x0F) << 8) | resp[1]
    return value

try:
    while True:
        adc_value = read_adc()
        print("ADC Value: %d" % adc_value)
        # Assuming a reference voltage of 3.3V for a full-scale reading
        voltage = (adc_value * 3.3) / 4095
        print("Potentiometer Voltage: %.2f" % voltage)
        time.sleep(0.5)

except KeyboardInterrupt:
    # Close SPI bus
    spi.close()
