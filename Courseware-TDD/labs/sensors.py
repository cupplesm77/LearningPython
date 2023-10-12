# sensors.py
from dataclasses import dataclass


def dbconnect(address=None, username=None, password=None):
    info_list = [address, username, password]
    print(info_list)
    dummy_initial_value_from_database = []
    return dummy_initial_value_from_database


@dataclass
class Datastore:
    address: str = None
    username: str = None
    password: str = None

    def __post_init__(self):
        self.conn = dbconnect(self.address, self.username, self.password)
        self.call_count = 0

    def record_datapoint(self, datum):
        # self.conn.append(datum)
        # self.call_count += 1
        pass

    def fetch(self, num_records):
        record_values = self.conn[-num_records:]
        return record_values


@dataclass
class Sensor:
    name: str
    datastore: object

    def receive(self, datum):
        self.datastore.record_datapoint(datum)

    def recent(self, timepoints):
        return self.datastore.fetch(timepoints)
