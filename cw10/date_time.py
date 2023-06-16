import datetime
import sys
import argparse


# Question 1

# now = datetime.datetime.now()
# print(now)

# Question 2

# dt1_str = sys.argv[1]
# dt2_str = sys.argv[2]

# dt1 = datetime.datetime.strptime(dt1_str, "%Y-%m-%d")
# dt2 = datetime.datetime.strptime(dt2_str, "%Y-%m-%d")


# print(dt2 - dt1)

# Question 3
parser = argparse.ArgumentParser()
parser.add_argument("--date")
parser.add_argument("--inputformat")
parser.add_argument("--outputformat")

args = parser.parse_args()

date_str = args.date
date_obj = datetime.datetime.strptime(date_str, args.inputformat)
new_date_str = date_obj.strftime(args.outputformat)
print(new_date_str)

# "%Y-%m-%d"
# "%d-%b-%Y"