# doing it without csv module for the fun of it
from statistics import mean


def val_sort(list_to_sort):
    """
    Args:
        list_to_sort: a list of lists to be sorted by the second value in each list.

    Returns:
        a list sorted by the second value in each sublist.
    """
    list_to_sort.sort(key=lambda x: x[1])
    return list_to_sort


fp = 'PyBank/budget_data.csv'

# read the file
with open(fp) as f:
    # header = f.readlines()[:1]
    lines = f.readlines()
    header = lines.pop(0)

# split at each delimiter
splits = [i.split(',') for i in lines]
months = [i[0] for i in splits]
# convert money to a number and drop the \n at the end
money = [int(i[1][:-1]) for i in splits]

total_money = sum(money)
total_months = len(months)
zipped = list(zip(months, money))

# subtracting index i + i from index i
diff = [zipped[i + 1][1] - zipped[i][1] for i in range(len(zipped) - 1)]

#%%
# zip months and list together to id month with greatest changes
ordered = [[a, b] for a, b in list(zip(months, diff))]
# avg_diff = round(mean(diff), 2)

# wanted to make a function instead of just doing
# reordered = [[b, a] for a, b in ordered]
val_sort(ordered)
diff.sort()

# the monthly changes are indexed next to the beginning month, not the end month.
# The +1 moves the index along to the end month.
max_month = months[months.index(ordered[-1][0]) + 1].replace('-', ' ')
min_month = months[months.index(ordered[0][0]) + 1].replace('-', ' ')
max_val = '{:,}'.format(diff[-1])
min_val = '{:,}'.format(diff[0])


output_msg = f'The total amount of months is {total_months}.\n' \
             f'The total value is ${"{:,}".format(total_money)}\n' \
             f'The average change is ${"{:,}".format(avg_diff)} .\n' \
             f'The month with the biggest gain is {max_month} (${max_val}).\n' \
             f'The month with the biggest loss is {min_month} (${min_val}).'

with open('output_file.txt', 'w+') as f:
    f.write(output_msg)

print(
        output_msg
)
