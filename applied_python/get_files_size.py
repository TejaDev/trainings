# How to run this script:
# python get_files_size.py  --directory /etc 
# python get_files_size.py  --directory /etc --reverse

import os
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

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Script to list out files from given directory')

    parser.add_argument('--directory', '-d', required=True, help='Source directory')
    parser.add_argument('--reverse', '-v', action='store_true', help='If set, use descending order')

    args = parser.parse_args()

    print get_files_size(directory=args.directory, reverse=args.reverse)
