"""
Implement a recursive function with signature find(path, filename) that
reports all entries of the file system rooted at the given path having
the given file name.
"""
import os


def find(path, filename):
    if (os.path.basename(path) == filename):
        print(path)

    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath = os.path.join(path, file)
            find(childpath, filename)
