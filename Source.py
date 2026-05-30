import json
import csv
import pickle


# Create a base class called Source that has a read_file method

# Create subclasses for each file_type that implement their own read_file methods
#     You might need to add some helper methods as well to clean/process the file contents
class Source:

    def __init__(self, path):
        self.path = path
        self.contents = self.read_file(path)

    def read_file(self, path):
        raise NotImplementedError("subclasses must implement read_file")

