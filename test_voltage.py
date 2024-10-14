import math

from voltage import Reading


def test_reading(timestamp = 1., adc = 12):
    """
    """
    r = Reading(timestamp, adc)
    assert math.isclose(r.timestamp, timestamp)
    assert r.adc == adc

def test_reading_conversion(timestamp = 1., adc = 12):
    """
    """
    r = Reading(timestamp, adc)
    assert math.isclose(r.voltage(), Reading._adc_to_voltage(adc))
