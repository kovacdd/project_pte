import os
from src.MDFMeasurement import MDFMeasurement
from src.SQLDatabase import SQLDatabase
from src.Measurement import Measurement

"""
Main program - Read data from .mf4 format and store data in sqlite3 .db database
"""

print('Read data from .mf4 format')

def main():

    folder = 'data'
    files = []

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file = os.path.abspath(filepath)
            files.append(file)

    for file in files:
        mdfm = MDFMeasurement(file)
        data = mdfm.set_data()

        sqld = SQLDatabase('database.db')
        sqld.create_table('data')
        sqld.insert_all(data)

    sqld.print()
    sqld.close()

    print('Success!')

    msrm = Measurement('database.db')
    msrm.event_detection(1, 10, 'voznja')

if __name__=="__main__":
    main()
