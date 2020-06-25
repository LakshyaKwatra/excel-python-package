from helper import *


class Sheet:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_labels(self, sep = '>>'):
        return get_df_labels(self.data, sep)
    
    def __repr__(self):
        return f'Sheet: {self.name}'

class WorkBook:

    def __init__(self, filepath):
        """ Generic distribution class for calculating and
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
        """
        self.filepath = filepath
        self.data_dict = get_data_dict(filepath)
        self.sheets = []
        for sheet_name in list(self.data_dict.keys()):
            self.sheets.append(Sheet(sheet_name,self.data_dict[sheet_name]))
        self.num_sheets = len(self.sheets)
        
    def get_all_labels(self, sep = '>>'):
        label_dict = {}
        for sheet in self.sheets:
            label_dict[sheet.name] = sheet.get_labels(sep)
        return label_dict

    def __repr__(self):
        return f'WorkBook: {self.filepath} :: {self.num_sheets} sheets'
