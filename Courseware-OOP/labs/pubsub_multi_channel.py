# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:10:59 2023

Powerful Python
Pythonic Observer Pattern (viz. PubSub)
Multi-channel publisher

@author: gravi
"""


# Subscriber
class SubscriberOne:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got "update" message: {message}')


class SubscriberTwo:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f'{self.name} got "receive" message: {message}')


class SubscriberThree:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def new_event(event_type, message):
        return f'({event_type}) "{message}"'


# Publisher  (takes registrations for published events)
# assume two pub_channels for registering and publishing

class Publisher:
    def __init__(self, pub_channels):
        """create an empty channel/subscriber dictionary

        :type pub_channels: list
        """

        self.channels = {channel: dict() for channel in pub_channels}

    def register(self, channel, who, callback=None):
        if callback is None:
            callback = who.update
        subscribers = self.channels[channel]
        subscribers[who] = callback
        # print(self.pub_channels)

    def unregister(self, channel, who):
        subscribers = self.channels[channel]
        del subscribers[who]

    def dispatch(self, channel, message):
        subscribers = self.channels[channel]
        for callback in subscribers.values():
            callback(message)


# working body of PubSub for meal messages

# create the publisher
channels = ['lunch', 'dinner']
pub = Publisher(channels)

# create instances of subscribers
john = SubscriberOne('John')
alice = SubscriberOne('Alice')
sam = SubscriberTwo('Sam')

# register subscribers with publisher
#   def register(self, channel, who, callback=None):
pub.register('lunch', john)
pub.register('dinner', john)
pub.register('lunch', alice)
pub.register('lunch', sam, sam.receive)
pub.register('dinner', sam, sam.receive)

pub.dispatch('lunch', 'Time for lunch!')
print('')
pub.dispatch('dinner', 'Time for dinner')
print('')

# unregister John
pub.unregister('dinner', john)
pub.dispatch('lunch', 'Time for lunch!')
print('')
pub.dispatch('dinner', 'Time for dinner')

# Note that callback can be ANY callable:
todd = SubscriberThree('Todd')


def todd_callback(message):
    print(todd.name + ' got "new_event" message: ' + todd.new_event('mealtime', message))


pub.register('dinner', todd, todd_callback)

pub.dispatch('dinner', 'Dinner is Ready!')
