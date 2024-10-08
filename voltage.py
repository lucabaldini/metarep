from dataclasses import dataclass

from loguru import logger
import numpy as np

@dataclass
class Reading:

    """Small container class representing a single voltage reading.
    """

    timestamp: float
    adc: int

    def voltage(self):
        """Convert ADC counts to a physical voltage (in V).
        """
        return 1.653 * self.adc + 0.456



class VoltageData:

    """Simple interface to a set of voltage readings.
    """

    def __init__(self, timestamps, adcs):
        logger.info(f'Initializing {self.__class__.__name__} from arrays...')
        self._readings = [Reading(timestamp, adc) for (timestamp, adc) in zip(timestamps, adcs)]
        logger.info(f'Done, {len(self._readings)} values read.')
        self._iterator = iter(self._readings)

    @classmethod
    def from_file(cls, file_path):
        logger.info(f'Reading voltage data from {file_path}...')
        timestamps = []
        adcs = []
        with open(file_path) as input_file:
            for line in input_file.readlines():
                timestamp, adc = cls._parse_line(line)
                timestamps.append(timestamp)
                adcs.append(adc)
        return cls(timestamps, adcs)

    @staticmethod
    def _parse_line(line):
        """Parse a single line from a text file and return a Reading object.
        """
        timestamp, adc = line.split()
        timestamp = float(timestamp)
        adc = int(adc)
        return timestamp, adc

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iterator)

    def __getitem__(self, index):
        return self._readings[index]




if __name__ == '__main__':
    t = np.linspace(1., 10., 10)
    a = np.full(t.shape, 127)
    data1 = VoltageData(t, a)
    for reading in data1:
        print(reading, reading.timestamp, reading.adc, reading.voltage())

    data2 = VoltageData.from_file('voltage_data.txt')
    for reading in data2:
        print(reading, reading.timestamp, reading.adc, reading.voltage())
    #
    # print('Done.')
    # print(data[3])
    #
    # print(data._parse_line('1. 127'))
    # print(VoltageData._parse_line('1. 127'))
