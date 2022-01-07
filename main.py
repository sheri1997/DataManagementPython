import pandas as pd
import numpy as np


class DataManagement:
    file1 = 'D:/BrizePython/DataManagementPython/MFG10YearTerminationData.csv'
    file2 = 'D:/BrizePython/DataManagementPython/MFG10YearTerminationData 2.csv'

    def reading_csv(self):
        """
        Here We are just reading the data from the location
        :return: will return the data in the csv format
        """
        data1 = pd.read_csv(self.file1)
        data2 = pd.read_csv(self.file2)
        return data1, data2

    def concat_csv(self):
        """
        Here We are performing the concat functions on the dataset
        :return: will return the concatenated dataframe
        """
        dataframe = pd.concat(map(pd.read_csv, [self.file1, self.file2]), ignore_index=True)
        return dataframe

    @staticmethod
    def operations_csv():
        """
        Here We are Just Performing different operations on the dataframe
        :return: Will return different operations performed
        """
        instance = DataManagement()
        dataframe = instance.concat_csv()
        print(dataframe.head)
        print(dataframe.tail)
        print(dataframe.shape)
        print(dataframe.dtypes)
        print(dataframe['EmployeeID'])
        print(dataframe[['EmployeeID', 'STATUS']])


ss = DataManagement.operations_csv()
print(ss)
