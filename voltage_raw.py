

file_path = 'voltage_data.txt'

def adc_to_voltage(adc):
    """Convert ADC counts to a physical voltage (in V).
    """
    return 1.653 * adc + 0.456


input_file = open(file_path)
for line in input_file.readlines():
    timestamp, adc = line.split()
    timestamp = float(timestamp)
    adc = int(adc)
    voltage = adc_to_voltage(adc)
    print(timestamp, adc, voltage)
