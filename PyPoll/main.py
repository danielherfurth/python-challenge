import csv, collections
# from datetime import datetime as dt


# start = dt.now()
# file to read
fp = 'PyPoll/election_data.csv'
name_list = []
header = []
with open(fp) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    header = next(reader)  # read headers
    for row in reader:
        name_list.append(row[1])  # only read the last name because it's faster and gets same results

# make a dictionary with a count of unique values
count_dict = collections.Counter(name_list)

# sum each candidate's votes'
total_votes = sum(count_dict.values())

# make the total easily human readable
total_vote_str = '{:,}'.format(sum(count_dict.values()))

# switch keys and values and place in list so that
# the list can be sorted to find the winner
n = [[v, k] for k, v in count_dict.items()]
n.sort(reverse=True)  # descending list

# make a string of 20 dashes similar to the picture in the readme
dashes = '-' * 20

# build the string that the script will output

output_msg = f'{dashes}\n' \
             f'Total Votes: {total_vote_str}\n' \
             f'{dashes}\n'

for k, v in count_dict.items():
    msg = f'{k} received {"{:.3%}".format(v / total_votes)} ({"{:,}".format(v)})\n'
    output_msg = output_msg + msg

output_msg = output_msg + f'{dashes}\n' + f'Winner: {n[0][1]}\n' + dashes

print(output_msg)

with open('PyPoll/text_file.txt', 'w+') as text_file:
    text_file.write(output_msg)

end = dt.now()

# print(end - start)


# the below code was commented out because of how slow it is.
# from datetime import datetime as dt
#
# start = dt.now()
# fp = 'PyPoll/election_data.csv'
#
# with open(fp) as f:
#     data = f.readlines()[1:]
#
# splits = [i.split(',') for i in data]
#
#
# names = [i[2][:-1] for i in splits]
# name_list = []
#
# [name_list.append(i) for i in names if i not in name_list]
# count_list = [[x, names.count(x)] for x in set(names)]
# total = sum([name[1] for name in count_list])
# percentages = [count[1]/total*100 for count in count_list]
#
# output_list = list(zip(name_list, percentages))
# dashes = '-'*20
#
# with open('file.txt', 'w+') as f:
#     total_str = f'Total Votes: {"{:,}".format(total)}'
#
#     f.write(dashes)
#     f.write(total_str)
#     f.write(dashes)
#
#     print(dashes)
#     print(total_str)
#     print(dashes)
#
#     for i in range(len(name_list)):
#         msg = f'{name_list[i]}: {round(percentages[i], 2)}% ({"{:,}".format(count_list[i][1])})'
#         print(msg)
#         f.write(msg)
#
#     print(dashes)
#     print(f'Winner: {name_list[0]}')
#     print(dashes)
#
#     f.write(dashes)
#     f.write(f'Winner: {name_list[0]}')
#     f.write(dashes)
#
# end = dt.now()
#
# print(end-start)