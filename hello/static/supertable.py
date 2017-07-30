#!/usr/bin/python3

import csv

f107 = open('ipgod107.csv')
f122 = open('ipgod122a.csv')
super = open('supertable.csv', 'w')

reader107 = csv.reader(f107)
reader122 = csv.reader(f122)
superwriter = csv.writer(super)

count = 0
for line107 in reader107:
	f122.seek(0)
	for line122 in reader122:
		if line107[0] == line122[0]:
			count = count + 1
			if count % 100 == 0:
				print(count)
			# [Application Number, Status, Category, Abstract]
			superwriter.writerow([line107[0], line107[9], line107[6], line122[1]])
			break

