#!/usr/bin/env python3
"""
filewatch.py

Use the observer pattern to implement an application that can watch a file's size change.

Requirements:
1) Write a program called `filewatch_extra.py`, that watches a file's size.
2) Run this file on the command line.
3) File will take one argument: the file to watch.
4) create two observer objects, named after people: "Bob" and "Stacy".
5) Both watchers will subscribe to the `FileWatcher` instance.
6) When informed that the file has changed, each observer will
print a message like the following to standard out:

Extra Credit
Make a copy of 'filewatch.py', named 'filewatch_extra.py'.  In this
new file, modify your program to distinguish between two types of
changes: increases in filesize, and decreases in filesize.

Let observers subscribe to one type of event, or both.  Create these
three observers:

 1) Bob is notified of file size increases,
 2) Stacy is notified of file size decreases,
 3) John is notified of any change at all.

The output for an increase event will look like:

----
Bob noticed the file increased to 4 bytes
John noticed the file increased to 4 bytes
----

For a decrease, it looks like:

----
Stacy noticed the file decreased to 4 bytes
John noticed the file decreased to 4 bytes
----

----
message example: Bob noticed the file is now 4 bytes
"""
# imports
import sys
import os
import time


def does_file_exist(file_to_watch):
    file_exists = os.path.exists(file_to_watch)
    print(f' file to watch: {file_to_watch}')
    if file_exists is False:
        print(f"File to watch file does not exist...exiting the program")
        sys.exit(1)
    else:
        print(f'file to watch exists: {file_to_watch}')


# setup file to watch
# file_to_watch = sys.argv[1]
# file_to_watch = 'no_file.txt'
file_to_watch = 'watched_file.txt'
does_file_exist(file_to_watch)


# classes

class FileWatcher:
    """
    class keeps polling a specific file
    """

    def __init__(self, path_of_file_to_watch, channels):
        self._channels = channels
        self.path = path_of_file_to_watch
        # create an empty subscriber's list
        self.subscribers = {channel: set() for channel in channels}
        self._filesize = os.stat(self.path).st_size

    def register(self, who, channel):
        self.subscribers[channel].add(who)
        return 0

    def unregister(self, who, channel):
        self.subscribers[channel].discard(who)

    def dispatch(self, who, change, size):
        name = who.name
        channels = self._channels
        message = self._form_message(name, channels, change, size)
        if message:
            who.update(message)

    @staticmethod
    def _form_message(name, channels, change, size):
        if change in channels:
            if change == channels[0]:
                message = f'{name} noticed that the file size has increased to filesize = {size} bytes'
            elif change == channels[1]:
                message = f'{name} noticed that the file size has decreased to filesize = {size} bytes'
            return message
        elif change not in channels:
            return False

    def check_file_while(self, final_step):
        """
        continue to check the file size for a given number of seconds (final_step)
        :return: 0
        """
        step = 0
        sleep_time = 0.5
        while step < final_step:
            self.monitor_file_size()
            time.sleep(sleep_time)
            step += 1
        return 0

    def monitor_file_size(self):
        file_byte_size = os.stat(self.path).st_size
        if file_byte_size != self._filesize:
            if file_byte_size > self._filesize:
                change_flag = self._channels[0]
            else:
                change_flag = self._channels[1]
            for watcher in self.subscribers[change_flag]:
                self.dispatch(watcher, change_flag, file_byte_size)
            self._filesize = file_byte_size


class FileObserver:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def update(message):
        print(message)


# implementation of pubsub:
watch = FileWatcher(file_to_watch, ['increase', 'decrease'])
print(watch.path)
bob = FileObserver('Bob')
stacy = FileObserver('Stacy')
joe = FileObserver('Joe')
watch.register(bob, 'increase')
watch.register(bob, 'decrease')
watch.register(stacy, 'decrease')
watch.register(joe, 'increase')
watch.register(joe, 'decrease')

# print(watch.subscribers[0].__class__.__name__)
# print(watch.subscribers[1])

# check file size for seconds
seconds = 50
p = watch.check_file_while(seconds)
print(f"file watched for {seconds} seconds; return: {p}")
