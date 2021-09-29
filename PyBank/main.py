ist# %%
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


fp = 'budget_data.csv'

with open(fp) as f:
    lines = f.readlines()[1:]

splits = [i.split(',') for i in lines]
months = [i[0] for i in splits]
money = [int(i[1][:-1]) for i in splits]

total_money = sum(money)
total_months = len(months)
zipped = list(zip(months, money))

diff = [zipped[i + 1][1] - zipped[i][1] for i in range(len(zipped) - 1)]
ordered = [[a, b] for a, b in list(zip(months, diff))]
avg_diff = round(mean(diff), 2)

val_sort(ordered)
diff.sort()

max_month = months[months.index(ordered[-1][0]) + 1].replace('-', ' ')
min_month = months[months.index(ordered[0][0]) + 1].replace('-', ' ')
max_val = '{:,}'.format(diff[-1])
min_val = '{:,}'.format(diff[0])

output_msg = f'The total amount of months is {total_months}.\n' \
             f'The total value is ${"{:,}".format(total_money)} (${max_val}).\n' \
             f'The average change is ${"{:,}".format(avg_diff)} (${min_val}).\n' \
             f'The month with the biggest gain is {max_month}.\n' \
             f'The month with the biggest loss is {min_month}.'

with open('output_file.txt', 'w+') as f:
    f.write(output_msg)

print(
        output_msg
)
