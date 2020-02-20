import csv
from sys import argv


class GoogleTrendAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.table = []
        self.headers = []
        with open(filename, 'r') as f:
            self.title = f.readline().strip()
            f.readline()
            reader = csv.reader(f)
            self.headers = reader.__next__()
            for row in reader:
                self.table.append(row)

    def most_popular(self):

        """
        Return the string of the most popular bird
        """
        max_col_number = -1
        max_value = float("-inf")
        for row in self.table:
            for col_number in range(row):
                data = row[col_number]
                if col_number > 0:
                    data_float = float(data)
                    if data_float > max_value:
                        max_value = data_float
                        max_col_number = col_number
        return self.headers[max_col_number]


if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage is stats.py [filename]")
    analyzer = GoogleTrendAnalyzer(argv[1])
    print(analyzer.most_popular())
