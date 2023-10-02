#!/usr/bin/env python3
"""
filewatch.py

Use the observer pattern to implement an application that can watch a file's size change.

Requirements:
1) Write a program called `filewatch.py`, that watches a file's size.
2) Run this file on the command line.
3) File will take one argument: the file to watch.
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

# setup file to watch
# file_to_watch = sys.argv[1]
file_to_watch = 'watched_file.txt'
print(file_to_watch)


# classes

class FileWatcher:
    """
    class keeps polling a specific file
    """

    def __init__(self, path_of_file_to_watch):
        self.path = path_of_file_to_watch

        # create an empty subscriber's list
        self.subscribers = []

    def register(self, who):
        self.subscribers.append(who)

    def dispatch(self, who, message):
        who.update(message)

    def watch(self) -> object:
        """

        :rtype: object
        """
        step = 0
        with open(self.path, 'r') as file:
            first_position = file.tell()
            content = file.read()
            filesize0 = len(content)
            file.seek(first_position)
            while step <= 29:
                # content = file.read()
                time.sleep(1.0)
                file.seek(first_position)
                content = file.read()
                file.seek(first_position)
                filesize1 = len(content)
                filesize_diff = filesize1 - filesize0
                filesize0 = filesize1
                if filesize_diff == 0:
                    pass
                else:
                    byte_length_file = os.stat(self.path).st_size
                    for watcher in self.subscribers:
                        self.dispatch(watcher,
                                      f'{watcher.name} noticed that the file size has changed: filesize = '
                                      f'{byte_length_file} bytes')
                step += 1


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

watch.watch()
