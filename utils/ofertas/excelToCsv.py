import pandas as pd
import numpy as np
import sys
import os

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def convertExcelToCsv(excelPath):
    oldFileName = os.path.basename(excelPath)
    outputPath = os.path.splitext(excelPath)[0] + "-CONVERTED.csv"
    originalFile = pd.read_excel(excelPath)

    # Get table of courses
    coursesTable = originalFile.iloc[:, 10:22]

    # Drop empty rows
    coursesTable = coursesTable[coursesTable['Sede'].notna()]

    # Drop accents
    cols = coursesTable.select_dtypes(include=[object]).columns
    coursesTable[cols] = coursesTable[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    
    # Drop header
    new_header = coursesTable.iloc[0] 
    coursesTable = coursesTable[1:] 
    coursesTable.columns = new_header
    
    coursesTable.to_csv (outputPath, index = None, header=True)

    print(f"{bcolors.OKGREEN} {oldFileName} courses offer converted successfuly to csv.{bcolors.ENDC}")
  

if __name__ == "__main__":
    convertExcelToCsv(sys.argv[1])

    