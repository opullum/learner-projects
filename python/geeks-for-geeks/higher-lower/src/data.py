import json

# Class Data
# Contains functions to handle the .json files containing Person data
# Passed to various functions to persistently store Person data

class Data:
    loaded_data = {}

    def __init__(self):
        pass

    # Getter method to return the current data file
    #
    # Returns: dict (data file containing Persons for game)

    def get_data(self) -> dict:
        return []
    
    # Menu to select a new file from /resources folder
    # Player will select a given file index which will be placed in 
    # class attribute

    def load_file(self) -> None:
        pass
