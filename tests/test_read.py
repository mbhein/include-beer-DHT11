import pytest
import DHT11

def test_main(capsys):
    data_pin = 0
    temp, humidity = DHT11.read(data_pin)
    print('Ambient Temperature: ' + str(temp))
    print('Ambient Humidity: ' + str(humidity))
