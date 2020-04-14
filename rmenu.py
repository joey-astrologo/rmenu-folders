#!/usr/bin/env python3

import argparse
import os


def folders_to_numbers(dir_list):
    file_name = 2
    for folder in dir_list:
        if folder == '01':
            continue
        if file_name > 9:
            c_n = '' + str(file_name)
        else:
            c_n = '0' + str(file_name)
        os.rename(folder, c_n)
        print("Renamed %s to %s" % (folder, c_n))
        file_name += 1


def numbers_to_folders(dir_list):
    for folder in dir_list:
        if folder == '01':
            continue
        onlyfiles = [os.path.splitext(f)[0] for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and f != '.DS_Store']
        os.rename(folder, onlyfiles[0])
        print("Renamed %s to %s" % (folder, onlyfiles[0]))


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', help='Path with folders of games')
    parser.add_argument('--reverse', action='store_true',
                        help='Reverse folder naming')

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print('Could not find directory')
        exit()

    path = os.path.expanduser(args.path)
    os.chdir(path)
    dir_list = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

    if not args.reverse:
        folders_to_numbers(sorted(dir_list))
    else:
        numbers_to_folders(sorted(dir_list))


if __name__ == '__main__':
    main()
