#!/usr/bin/env python3
"""
filewatch.py

Use the observer pattern to implement an application that can watch_file a file's size change.

Requirements:
1) Write a program called `filewatch.py`, that watches a file's size.
2) Run this file on the command line.
3) File will take one argument: the file to watch_file.
4) create two observer objects, named after people: "Bob" and "Stacy".
5) Both watchers will subscribe to the `FileWatcher` instance.
6) When informed that the file has changed, each observer will
print a message like the following to standard out:
----
message example: Bob noticed the file is now 4 bytes
"""
# imports
import sys
import os
import time

# setup file to watch_file
file_to_watch = sys.argv[1]
# file_to_watch = 'watched_file.txt'
print(f' file to watch: {file_to_watch}')


# classes

class FileWatcher:
    """
    class keeps polling a specific file
    """

    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch
        # create an empty subscriber's list
        self.subscribers = []
        self._filesize = os.stat(self.path).st_size

    def register(self, who):
        self.subscribers.append(who)

    @staticmethod
    def dispatch(who, size):
        message = f'{who.name} noticed that the file size has changed: filesize = {size} bytes'
        who.update(message)

    def check_awhile(self, final_step):
        """
        continue to check the file size for a given number of seconds (final_step)
        :return: 0
        """
        step = 0
        sleep_time = 0.2
        while step < final_step:
            self.watch_file()
            time.sleep(sleep_time)
            step += 1
        return 0

    def watch_file(self):
        file_byte_size = os.stat(self.path).st_size
        if file_byte_size != self._filesize:
            self._filesize = file_byte_size
            for watcher in self.subscribers:
                self.dispatch(watcher, self._filesize)


class FileObserver:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def update(message):
        print(message)


# implementation of pubsub:
watch = FileWatcher(file_to_watch)
print(watch.path)
bob = FileObserver('Bob')
stacy = FileObserver('Stacy')
watch.register(bob)
watch.register(stacy)

print(watch.subscribers[0].__class__.__name__)
print(watch.subscribers[1])

# check file size for seconds
seconds = 70
p = watch.check_awhile(seconds)
print(f"file watched for {seconds} seconds; return: {p}")
