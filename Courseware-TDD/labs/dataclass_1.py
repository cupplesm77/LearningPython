# *******************************************************************
# a simple dataclass example based on pubsub
# can be compared to dataclass_2.py that does not implement dataclasses
from dataclasses import dataclass, field


# in the Observer class below:
# If eq is false, __hash__() will be left untouched meaning the __hash__() method of the superclass
# will be used ("if the superclass is object, this means it will fall back to id - based hashing").
# https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass


# @dataclass
# @dataclass(eq=False)
# @dataclass(unsafe_hash=True, eq=False)
@dataclass(unsafe_hash=True)
class Observer:
    name: str = field(default=None)

    @staticmethod
    def update(message):
        print(message)


@dataclass
class Observing:
    _channels: list = field(default_factory=list)

    def __post_init__(self):
        self.channel_dict = {channel: set() for channel in self._channels}

    def register(self, who, channel):
        assert isinstance(who, object)
        self.channel_dict[channel].add(who)

    def dispatch(self, who):
        who.update(self.channel_dict)
        # print(self.channel_dict)


channels = ["ONE", "two", "three", "four", "five"]

# publisher
observing = Observing(channels)

# subscribers
johndoe = Observer()  # added to indicate how the default subscriber is implemented
joe = Observer("Joe")
print(f"type of Joe: {type(joe)}")
ted = Observer("Ted")
sue = Observer("Sue")
rose = Observer("Rose")

observing.register(None, "five")
observing.register(johndoe, "five")
observing.register(joe, "two")
observing.register(joe, "four")
observing.register(ted, "two")
observing.register(ted, "ONE")
observing.register(sue, "three")
observing.register(sue, "ONE")
observing.register(rose, "ONE")
observing.register(rose, "two")
observing.register(rose, "three")
observing.register(rose, "four")
observing.register(rose, "five")

observing.dispatch(joe)

# demonstrate __repr__ and __str__
print("")
print(observing)
print("")
print(repr(observing))
