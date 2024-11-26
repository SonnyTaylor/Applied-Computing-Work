import csv


# Read from a file
def read_csv_file(file_name):
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


# Write to file
def write_csv_file(file_name, data_to_write):
    with open(file_name, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data_to_write)


print("Reading from file")
read_csv_file("data.csv")

print("Writing to file")
data = [["Name", "Age"], ["John", 25], ["Doe", 30]]
write_csv_file("output.csv", data)
