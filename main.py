import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb


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

    @staticmethod
    def matplot_graph_plot():
        """
        Here We are Plotting the graph for various tables of the graph
        :return: will return different graphs
        """
        instance = DataManagement()
        dataframe = instance.concat_csv()
        employee_data = dataframe['EmployeeID']
        status_year_data = dataframe['STATUS_YEAR']
        scatter_plot = plt.scatter(employee_data, status_year_data)
        return scatter_plot

    @staticmethod
    def seaborn_graph_plot():
        instance = DataManagement()
        dataframe = instance.concat_csv()
        gender_graph = sb.countplot('gender_full', data=dataframe)
        print(gender_graph)
        catplot_graph = sb.catplot(x='BUSINESS_UNIT', y='gender_full', data=dataframe)
        print(catplot_graph)
        barplot_graph = sb.barplot(x= 'age', y='EmployeeID', data=dataframe)
        print(barplot_graph)

    @staticmethod
    def duplicate_values():
        """
        Here We are finding the duplicated values in a particular column
        :return: will return boolean series denoting duplicated values.
        """
        instance = DataManagement()
        dataframe = instance.concat_csv()
        duplicate = dataframe[dataframe.duplicated('EmployeeID')]
        return duplicate

    @staticmethod
    def cardinality_values():
        """
        Here We are finding the cardinality of the rows and columns of the dataframe.
        :return: will return all the unique values inside the dataframe.
        """
        instance = DataManagement()
        dataframe = instance.concat_csv()
        cardinality_row = dataframe.nunique(axis=0, dropna=True)
        cardinality_column = dataframe.nunique(axis=1, dropna=True)
        return cardinality_row, cardinality_column



