# test_sensors.py

import unittest
from unittest.mock import Mock
import sensors


class TestSensors(unittest.TestCase):
    def test_record_data(self):
        # set up mock
        dstore = Mock(sensors.Datastore)
        dstore.fetch.return_value = [5, 6, 7, 8, 9]

        sensor = sensors.Sensor("Temperature", dstore)
        for x in range(10):
            sensor.receive(x)
        self.assertEqual([5, 6, 7, 8, 9], sensor.recent(5))

        # NOTE: One doesn't need to configure record_datapoint() to run this Mock
        # assert expected mock behavior
        self.assertEqual(10, dstore.record_datapoint.call_count)
        print(dstore.fetch.assert_called_once())
