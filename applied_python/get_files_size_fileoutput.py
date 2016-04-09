# SOLUTION

# How to run this script:
# python get_files_size.py  --directory /etc 
# python get_files_size.py  --directory /etc --reverse
# python get_files_size.py  --directory /etc --file_path /tmp/output

import sys
import os
import time
from collections import OrderedDict
from operator import itemgetter

def get_files_size(directory='/tmp', reverse=False):
    list_of_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path_to_file = os.path.join(root, file)
            if os.path.isfile(path_to_file):
                list_of_files.append((path_to_file, os.path.getsize(path_to_file)))

    return OrderedDict(sorted(list_of_files, key=itemgetter(1), reverse=reverse))

def get_timestamp():
    return int(time.time())


def write_to_file(file_path, dict_to_write):
    if not file_path:
        file_path = os.path.join('/tmp', "{}_files.out".format(get_timestamp()))

    try:
        with open(file_path, 'w') as f:
            for key, value in dict_to_write.items():
                f.write("{} {}\n".format(key, value))
    except IOError as exc:
        print "Cannot write output to file, ", exc
        sys.exit(1)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--reverse', '-v', action='store_true', help='If set, use descending order')
    parser.add_argument('--file_path', '-o', help='Output file path')

    args = parser.parse_args()

    files_size_dict = get_files_size(directory=args.directory, reverse=args.reverse)

    write_to_file(file_path=args.file_path, dict_to_write=files_size_dict)
