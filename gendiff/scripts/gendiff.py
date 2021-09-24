#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('fisrt_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format')


def main():
    parser.parse_args()
