import csv
import os


class ProfitCalculator:
    def __init__(self, filename):
        self.filename = filename
        self.total_profit = 0

    def calculate_profit(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    book_name = row[0]
                    purchase_price = float(row[3])
                    try:
                        sale_price = float(row[5])
                    except ValueError:
                        sale_price = 0.0
                    purchaser = row[4]

                    if purchaser != "NA":
                        profit = sale_price - purchase_price
                    else:
                        profit = -purchase_price

                    self.total_profit += profit
                    self.display_book_profit(book_name, profit)

                self.display_total_profit()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def display_book_profit(self, book_name, profit):
        print(f"Book: {book_name}, Profit/Loss: {profit}")

    def display_total_profit(self):
        print(f"Total Profit: {self.total_profit}")


while True:
    csv_file_path = input("Enter CSV file path: ")
    if not os.path.isfile(csv_file_path):
        print("Invalid file path.")
        continue

    calculator = ProfitCalculator(csv_file_path)
    calculator.calculate_profit()
