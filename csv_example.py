import csv
import pandas

filename = 'resources/data.csv'

# Using csv
r = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        r.append(row)

print(r)

# Using pandas
df = pandas.read_csv(filename)
print(df)
print(type(df['Salary'][0]))

df2 = pandas.read_csv('resources/test.csv')
print(f"data:{df2['Count'][0]} type:{type(df2['Count'][0])}")
print(f"data:{df2['Count'][10]} type:{type(df2['Count'][10])}")

df2 = pandas.read_csv('resources/test2.csv')
print(df2['BIN'].to_list())
print(type(df2['BIN'][0]))
print(f"data:{df2['% of total'].to_list()}")
