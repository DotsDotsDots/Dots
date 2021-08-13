titles = list()

# read titles from file

filename = 'titles.txt'
with open (filename) as fin:
    for line in fin:
        titles.append(line.strip())


# sort titles

titles.sort(reverse=True)
print(titles)

# write sorted titles to file

filename = 'Descending Alphabetically.txt'
with open(filename, 'w') as fout:
    for title in titles:
        fout.write(title + '\n') 