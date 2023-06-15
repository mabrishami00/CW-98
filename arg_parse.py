import argparse
import os

# Question 1

# parser = argparse.ArgumentParser()
# parser.add_argument("first_number", type=int)
# parser.add_argument("second_number", type=int)
# args = parser.parse_args()
# summation = args.first_number + args.second_number
# print(f"summation:{summation}")

# Question 2

# parser = argparse.ArgumentParser()
# parser.add_argument("path")
# args = parser.parse_args()
# path = args.path
# dirs = os.listdir(path)
# print(dirs)

# Question 3

parser = argparse.ArgumentParser()
parser.add_argument("--size", action="store_true")
parser.add_argument("path_inp")
args = parser.parse_args()
path_input = args.path_inp
dirs = os.listdir(path_input)

if args.size is True:
    for dir in dirs:
        size = os.path.getsize(dir)
        print(dir,": ", size)
else:
    for dir in dirs:
        print(dir)
    