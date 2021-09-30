import csv
from collections import Counter

# from datetime import datetime as dt
# start = dt.now()

# file to read
FP = 'PyPoll/election_data.csv'
name_list = []

with open(FP) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)  # read headers

    for row in reader:
        name_list.append(row[2])  # only read last name because it's faster and gets same results

# make a dictionary with a count of unique values
count_dict = Counter(name_list)

# sum each candidate's votes'
total_votes = sum(count_dict.values())

# make the total easily human readable
TOTAL_VOTE_STR = '{:,}'.format(sum(count_dict.values()))

# person with most votes
winner = Counter(name_list).most_common(1)[0][0]

# make a string of 20 dashes similar to the picture in the readme
DASHES = '-' * 20

# build the string that the script will output
output_msg = 'ELECTION RESULTS\n' \
             f'{DASHES}\n' \
             f'Total Votes: {TOTAL_VOTE_STR}\n' \
             f'{DASHES}\n'

for k, v in count_dict.items():
    msg = f'{k} received {"{:.3%}".format(v / total_votes)} ({"{:,}".format(v)}).\n'
    output_msg = output_msg + msg

output_msg = output_msg + f'{DASHES}\n' + f'Winner: {winner}\n' + DASHES

print(output_msg)

with open('PyPoll/text_file.txt', 'w+') as text_file:
    text_file.write(output_msg)

# end = dt.now()

# print(end - start)
# 1.576352 s to run

# region
# the below code was commented out because of how slow it is.
# from datetime import datetime as dt
#
# start = dt.now()
# FP = 'PyPoll/election_data.csv'
#
# with open(FP) as f:
#     data = f.readlines()[1:]
#
# splits = [i.split(',') for i in data]
#
# names = [i[2][:-1] for i in splits]
# name_list = []
#
# [name_list.append(i) for i in names if i not in name_list]
# count_list = [[x, names.count(x)] for x in set(names)]
# total = sum([name[1] for name in count_list])
# percentages = [count[1] / total * 100 for count in count_list]
#
# output_list = list(zip(name_list, percentages))
# DASHES = '-' * 20
#
# with open('file.txt', 'w+') as f:
#     total_str = f'Total Votes: {"{:,}".format(total)}'
#
#     f.write(DASHES)
#     f.write(total_str)
#     f.write(DASHES)
#
#     print(DASHES)
#     print(total_str)
#     print(DASHES)
#
#     for i in range(len(name_list)):
#         msg = f'{name_list[i]}: {round(percentages[i], 2)}% ({"{:,}".format(count_list[i][1])})'
#         print(msg)
#         f.write(msg)
#
#     print(DASHES)
#     print(f'Winner: {name_list[0]}')
#     print(DASHES)
#
#     f.write(DASHES)
#     f.write(f'Winner: {name_list[0]}')
#     f.write(DASHES)
#
# end = dt.now()
#
# print(end - start)
# 4.079913 s to run
# endregion
