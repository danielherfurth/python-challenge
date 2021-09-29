fp = 'election_data.csv'

with open(fp) as f:
    data = f.readlines()[1:]

splits = [i.split(',') for i in data]


names = [i[2][:-1] for i in splits]
name_list = []

[name_list.append(i) for i in names if i not in name_list]
count_list = [[x, names.count(x)] for x in set(names)]
total = sum([name[1] for name in count_list])
percentages = [count[1]/total*100 for count in count_list]

output_list = list(zip(name_list, percentages))
dashes = '-'*20

with open('file.txt', 'w+') as f:
    total_str = f'Total Votes: {"{:,}".format(total)}'

    f.write(dashes)
    f.write(total_str)
    f.write(dashes)

    print(dashes)
    print(total_str)
    print(dashes)

    for i in range(len(name_list)):
        msg = f'{name_list[i]}: {round(percentages[i], 2)}% ({"{:,}".format(count_list[i][1])})'
        print(msg)
        f.write(msg)

    print(dashes)
    print(f'Winner: {name_list[0]}')
    print(dashes)

    f.write(dashes)
    f.write(f'Winner: {name_list[0]}')
    f.write(dashes)