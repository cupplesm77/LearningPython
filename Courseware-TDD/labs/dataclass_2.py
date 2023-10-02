# *******************************************************************
# a simple pubsub case:
# doesn't use dataclasses
# used to compare to dataclass_1.py that DOES use dataclasses


class Observer:
    """
    Observer is the "Subscriber"
    :type name: str
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def update(message):
        print(message)


class Observing:
    _observing_channels: list[str] = ["ONE", "two", "three", "four", "five"]

    def __init__(self):
        self.channel = {channel: set() for channel in self._observing_channels}

    def register(self, who, channel):
        assert isinstance(who, object)
        self.channel[channel].add(who)

    def unregister(self, who, channel):
        subscribers = self.channel[channel]
        del subscribers[who]

    def dispatch(self, who):
        who.update(self.channel)
        # print(self.channel)


observing = Observing()

joe = Observer("Joe")
print(f"type of Joe: {type(joe)}")
ted = Observer("Ted")
sue = Observer("Sue")
rose = Observer("Rose")

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

print("")
print(repr(observing))
