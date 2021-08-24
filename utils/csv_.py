import csv


class CSV(object):

    EXTENSION = ['.csv', ]

    def __init__(self):

        pass

    @staticmethod
    def read(file_):
        """
        Read csv file

        """
        with open(file_, newline="") as fp:
            content = csv.DictReader(fp)
            # df = pd.read_csv(fp, delimiter=',', index_col='Name')
            for row in content:
                print(f"{row['Name']} is {row['Sex']} and age is {row['Age']}")

    @staticmethod
    def write(file_):
        """
        Write csv file

        """
        with open(file_, 'w') as fp:
            handle = csv.DictWriter(fp, fieldnames=['Name', 'Age', 'Sex'])
            handle.writeheader()
            handle.writerow({'Name': 'Milton', 'Sex': 'Male', 'Age': 29})


# csv_file = CSV()
# csv_file.read('C:/Users/Milton Savarimuthu/PycharmProjects/Project/Logs/sample.csv')
