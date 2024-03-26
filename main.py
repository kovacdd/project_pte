import os
import matplotlib.pyplot as plot
import numpy as np

from src.MDFMeasurement import MDFMeasurement
from src.SQLDatabase import SQLDatabase
from src.Measurement import Measurement

"""
Main program - Milestone 1, 2, 3
"""

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

    print('End of Milestone 1')

    msrm = Measurement('database.db')
    results = msrm.event_detection(1, 10, 'voznja')

    print('End of Milestone 2')

    for point in range(len(results)):
        x = np.array(results[point][3])
        y = np.array(results[point][2])

    plot.plot(x, y)
    plot.show()

    print('End of Milestone 3')

if __name__=="__main__":
    main()
