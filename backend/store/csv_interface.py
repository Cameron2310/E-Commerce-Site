import csv


class CSV_Interface:

    def __init__(self, filename):

        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            self.column_names = reader.fieldnames

        self.filename = filename
        self.update_data()

    @property
    def all_data(self):
        self.update_data()
        return self.__all_data

    @all_data.setter
    def all_data(self, val):
        self.__all_data = val

    # read data from the file
    # update the all_data list
    # return the new list

    def update_data(self):

        data = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        self.__all_data = data
        return self.__all_data

    # append a singular row to a CSV file
    def append_one_row_to_file(self, new_data_dict):

        with open(self.filename, "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.column_names)
            writer.writerow(new_data_dict)

        return self.all_data

    # rewrite the csv file with new data
    def update(self, header, data):

        with open(self.filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    def filter_products(self, filter_by, name):
        data = self.all_data
        filtered_products = []

        for i in range(len(data)):
            if data[i][filter_by] == name:
                filtered_products.append(data[i])

        return filtered_products

    def get_by_id(self, data, id):
        '''Get data from 1 CSV file, which has a relationship to another CSV file'''

        for i in range(len(data)):
            if data[i]['id'] == id:
                return data[i]

        return 'Item not in inventory'

    def update_quantity(self, id, new_quantity):
        with open(self.filename, newline='') as csvfile:
            readData = [row for row in csv.DictReader(csvfile)]

        for i in range(len(readData)):
            if readData[i]['id'] == str(id):
                readData[i]['quantity'] = new_quantity
                readHeader = readData[i].keys()

        self.update(readHeader, readData)

    def delete_row(self, id):
        with open(self.filename, newline='') as csvfile:
            csvreader = csv.DictReader(
                csvfile, fieldnames=self.column_names)
            output = [x for x in csvreader if x['id'] != str(id)]

        with open(self.filename, 'w', newline='') as csvfile:
            csvreader = csv.DictWriter(
                csvfile, fieldnames=self.column_names)

            for x in output:
                csvreader.writerow(x)
