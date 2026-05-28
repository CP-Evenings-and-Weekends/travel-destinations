import json
import csv
import pickle
import pandas as pd


# Create a base class called Source that has a read_file method

# Create subclasses for each file_type that implement their own read_file methods
#     You might need to add some helper methods as well to clean/process the file contents
class Source:

    def __init__(self, file_type):
        self.file_type = file_type
        self.contents = self.read_file()

    def read_file(self):
        return ???

