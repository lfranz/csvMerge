import csv, sys, os
from sys import platform as _platform

list_input = []


def column(matrix, i):
	return [row[0:i] for row in matrix]


file_input = sys.argv[1]

path = os.path.split(file_input)
file_path = os.path.splitext(path[1])
filename = file_path[0]
extension = file_path[1]
filename_out = str(path[0]) + "\\" + str(filename) + "_new" + str(extension)

if _platform == "linux" or _platform == "linux2":
	os.system('clear')
elif _platform == "darwin":
	os.system('clear')
elif _platform == "win32":
	os.system('cls')

num_columns = input("How many columns do you want to keep? (0 for all): ")

with open(file_input, 'rb') as file_csv:
	reader = csv.reader(file_csv, delimiter='\t')
	for row in reader:
		list_input.append(row)

if len(sys.argv) > 2:
	for single_file in sys.argv[2:]:
		with open(single_file, 'rb') as file_csv:
			reader = csv.reader(file_csv, delimiter='\t')
			first_row = next(reader)
			for row in reader:
				list_input.append(row)

if num_columns != 0:
	list_output = column(list_input, num_columns)
else:
	list_output = list_input

with open(filename_out, 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row in list_output:
		spamwriter.writerow(row)
