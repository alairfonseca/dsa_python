# File systems
import os


def disk_usage(path):
    total = os.path.getsize(path)

    if os.path.isdir(path):
        for file_path in os.listdir(path):
            child_path = os.path.join(path, file_path)

            total += disk_usage(child_path)

    print("{0:<7}".format(total), path)
    return total
