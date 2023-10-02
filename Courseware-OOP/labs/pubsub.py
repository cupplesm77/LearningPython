# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:10:59 2023

Powerful Python
Pythonic Observer Pattern (viz. PubSub)

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


def todd_callback(message):
    print(todd.name + ' got "new_event "message: ' + todd.new_event('mealtime', message))


# Publisher  (takes registrations for published events)
# assume two pub_channels for registering and publishing
class Publisher:
    def __init__(self):
        # create an empty subscriber's dictionary
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None:
            callback = who.update
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for callback in self.subscribers.values():
            callback(message)


# working body of PubSub
# PubSub for meal messages
# Using:

# create instances of subscribers
john = SubscriberOne('John')
alice = SubscriberOne('Alice')
sam = SubscriberTwo('Sam')

# create the publisher
pub = Publisher()

# register subscribers with publisher
pub.register(john)
pub.register(alice)
pub.register(sam, sam.receive)

pub.dispatch('Time for lunch!')
print('')
pub.dispatch('Time for dinner')
print('')

# unregister John
pub.unregister(john)
pub.dispatch('Time for lunch!')
print('')
pub.dispatch('Time for dinner')

# Note that callback can be ANY callable:
todd = SubscriberThree('Todd')
pub.register(todd, todd_callback)
pub.dispatch('Breakfast is Ready!')
