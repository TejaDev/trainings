import argparse

parser = argparse.ArgumentParser(description='Script to list out files from given directory')

parser.add_argument('--directory', '-d', required=True, help='Source directory')
parser.add_argument('--verbose', '-v', action='store_true', help='If set, print more details')

args = parser.parse_args()

print "directory: ", args.directory
print "verbose:   ", args.verbose
