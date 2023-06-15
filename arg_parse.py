import argparse
import os

# Question 1

parser = argparse.ArgumentParser()
parser.add_argument("first_number", type=int)
parser.add_argument("second_number", type=int)
args = parser.parse_args()
summation = args.first_number + args.second_number
print(f"summation:{summation}")

#Question 2


