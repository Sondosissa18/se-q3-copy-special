#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "sondos with help from john , gabby, shanquel and piero"

import re
# import os
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    for root, dirs, files in os.walk(os.path.abspath(dirname)):
        for name in files:
            if re.findall(r'__(\w+)__', name):
                result.append(os.path.join(root, name))
        break
    return result


def copy_to(path_list, dest_dir):
    ''' copy file to folder if it the folder does not exist create a file'''

    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    ''' zip from one file to another'''
    command_list = ["zip", "-j", dest_zip]
    command_list.extend(path_list)
    subprocess.run(command_list)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='source to read from')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # TODO: you must write your own code to get the command line args.
    special_list = get_special_paths(ns.fromdir)
    if ns.todir is not None:
        copy_to(special_list, ns.todir)
    elif ns.tozip is not None:
        zip_to(special_list, ns.tozip)
    else:
        print('\n'.join(special_list))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python copyspecial.py file-to-copy')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
