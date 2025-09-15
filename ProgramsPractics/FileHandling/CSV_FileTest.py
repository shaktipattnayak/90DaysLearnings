import csv

output_file = 'ouput.csv'

# Writing to a CSV file
new_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 28, "Sydney"]
]

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(new_data)

print(f"Data written to {output_file} successfully!")

# Reading from CSV file
# Reading from a CSV file
with open(output_file, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Read header row
    rows = [row for row in csv_reader]

print("Header:", header)
print("Data:")
for row in rows:
    print(row)
