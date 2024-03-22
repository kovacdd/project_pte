from src.MDFMeasurement import MDFMeasurement
from src.SQLDatabase import SQLDatabase

"""
Main program - Read data from .mf4 format and store data in sqlite3 database
"""

print('Read data from .mf4 format')

def main():

    file1 = 'C:/Users/u22k86/project_pte/data/Fzg01_40402_1.mf4'
    file11 = 'C:/Users/u22k86/project_pte/data/Fzg01_40403_1.mf4'

    file2 = 'C:/Users/u22k86/project_pte/data/Fzg02_40402_1.mf4'
    file21 = 'C:/Users/u22k86/project_pte/data/Fzg02_40402_2.mf4'
    file22 = 'C:/Users/u22k86/project_pte/data/Fzg02_40402_3.mf4'
    file23 = 'C:/Users/u22k86/project_pte/data/Fzg02_40403_1.mf4'
    file24 = 'C:/Users/u22k86/project_pte/data/Fzg02_40403_2.mf4'
    file25 = 'C:/Users/u22k86/project_pte/data/Fzg02_40403_3.mf4'

    file3 = 'C:/Users/u22k86/project_pte/data/Fzg03_40402_1.mf4'
    file31 = 'C:/Users/u22k86/project_pte/data/Fzg03_40402_2.mf4'
    file32 = 'C:/Users/u22k86/project_pte/data/Fzg03_40402_3.mf4'
    file33 = 'C:/Users/u22k86/project_pte/data/Fzg03_40403_1.mf4'
    file34 = 'C:/Users/u22k86/project_pte/data/Fzg03_40403_2.mf4'
    file35 = 'C:/Users/u22k86/project_pte/data/Fzg03_40403_3.mf4'

    # files = [file1, file2, file3]
    files1 = [file1, file11, file2, file21, file22, file23, file24, file25, file3, file31, file32, file33, file34, file35]
    files = files1
    
    for file in files:
        mdfm = MDFMeasurement(file)
        data = mdfm.set_data()

        sqld = SQLDatabase('database.db')
        sqld.create_table('data')
        sqld.insert_all(data)

    sqld.print()
    sqld.close()

    print('Success!')

if __name__=="__main__":
    main()
