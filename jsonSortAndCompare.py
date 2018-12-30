import os, sys
import argparse
import json
import subprocess

def walkDown(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".json"):
                yield os.path.abspath(os.path.join(root, f))
        for d in dirs:
            walkDown(os.path.join(root, d))

def openAndSort(file):
    with open(file) as file1:
        firstJson = json.load(file1)

    with open(file, "w+") as newfile1:
        json.dump(firstJson, newfile1, sort_keys=True, indent=2)

if __name__ == '__main__':
    argv = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=False, nargs=argparse.REMAINDER)
    parser.add_argument("--jsons", required = False, nargs = argparse.REMAINDER)

    files = vars(parser.parse_args(argv))["jsons"]
    dir = vars(parser.parse_args(argv))["dir"]
    jsons_dir_path = dir[0] if dir is not None else os.path.dirname(os.path.realpath(__file__))

    if files is not None:
        print("Working with specified Json files ...")
        for j in files:
            openAndSort(j)
    else:
        print("Working with all Json files in the directory ...")
        for j in walkDown(jsons_dir_path):
            openAndSort(j)

    print("DONE : All Sorted !")