#!/usr/bin/env python3

# The script for generating 2 CSV files with reports from /log/syslog about
# activity of example service 'ticky'. 'error_file' will contain error messages
# and their counts in log sorted by frequency. 'user_file' will contain counts
# of INFO and ERROR messages generated by activity of each user, sorted by 
# username

import operator
import re
import csv

filename = "syslog.log"

def process_reports(source):
    per_user = {}
    errors = {}
    error_pat = r"ticky: ERROR ([\w' ]+)"
    info_pat = r"ticky: INFO ([\w' ]+)"
    usr_pat = r"\(([\w.]+)\)"
    with open(source) as f:
        for line in f:
            line = line.strip()
            # process error
            match_err = re.search(error_pat, line)
            if match_err:
                err = match_err.group(1)
                errors[err] = errors.get(err, 0) + 1
                usr = re.search(usr_pat, line).group(1)
                if usr not in per_user:
                    per_user[usr] = [0, 0]
                per_user[usr][0] += 1

            # process info
            match_inf = re.search(info_pat, line)
            if match_inf:
                inf = match_inf.group(1)
                usr = re.search(usr_pat, line).group(1)
                if usr not in per_user:
                    per_user[usr] = [0, 0]
                per_user[usr][1] += 1

    return errors, per_user

errors, per_user = process_reports(filename)

def generate_reports(errors, per_user, error_file, user_file):
    errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
    per_user = sorted(per_user.items())
    error_table = [["Error", "Count"]]
    for tup in errors:
        error_table.append([tup[0].strip(), tup[1]])
    user_table = [["Username", "INFO", "ERROR"]]
    for tup in per_user:
        user_table.append([tup[0], tup[1][1], tup[1][0]])
    return error_table, user_table 

error_table, user_table = generate_reports(errors, per_user,"",  "user_statistics.csv")

error_file = "error_message.csv"
user_file = "user_statistics.csv"

with open(error_file, "w") as f:
    writer = csv.writer(f)
    for line in error_table:
        writer.writerow(line)

with open(user_file, "w") as f:
    writer = csv.writer(f)
    for line in user_table:
        writer.writerow(line)
