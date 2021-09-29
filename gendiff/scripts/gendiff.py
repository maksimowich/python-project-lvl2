#!/usr/bin/env python
import argparse
from gendiff.gendiff import generate_diff

parser = argparse.ArgumentParser()

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', nargs='?', default='stylish')


def main():
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
