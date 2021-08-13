titles = list()

# read titles from file

filename = 'titles.txt'
with open (filename) as fin:
    for line in fin:
        titles.append(line.strip())


# sort titles

titles.sort()
print(titles)

# write sorted titles to file

filename = 'Ascending Alphabetically.txt'
with open(filename, 'w') as fout:
    for title in titles:
        fout.write(title + '\n') 