import os
import bs4
import wget
import requests
import pandas as pd
import matplotlib.pyplot as plt

from pdfminer.high_level import extract_text

WEB_PAGE_ROOT = "https://www.education.ie/en/Publications/Inspection-Reports-Publications/Whole-School-Evaluation-Reports-List/?pageNumber="
NUMBER_OF_PAGES = 5
PATH_TO_ALL_REPORTS = "./Reports"
PATH_TO_PDF_REPORTS = PATH_TO_ALL_REPORTS + "/pdf"
PATH_TO_TEXT_REPORTS = PATH_TO_ALL_REPORTS + "/plain_text"

General_InspectionReports = pd.DataFrame(columns=['Date','School Roll No.','County','School Name','School Level','Inspection Type','Subject','URL'])

if os.path.exists(PATH_TO_ALL_REPORTS) == False: os.mkdir(PATH_TO_ALL_REPORTS)
if os.path.exists(PATH_TO_PDF_REPORTS) == False: os.mkdir(PATH_TO_PDF_REPORTS)

# Turn web table into Datafram
for pageNumber in range(1, NUMBER_OF_PAGES + 1):
    IrelandWebpage = requests.get(WEB_PAGE_ROOT + str(pageNumber))
    CleanIrelandWebpage = bs4.BeautifulSoup(IrelandWebpage.text, "lxml")
    InspectionReports = {}
    ID = 0
    Table = CleanIrelandWebpage.find('table', id="IRList")
    for p in Table.find_all('tr'):
        if ID == 0:
            ID = ID + 1
            continue
        else:
            Date = p('td')[0].string[:2] + '_' + p('td')[0].string[3:5] + '_' + p('td')[0].string[6:]
            SchoolRoll = p('td')[1].string
            County = p('td')[2].string
            SchoolName = p('td')[3].string
            SchoolLevel = p('td')[4].string
            InspectionType = p('td')[5].string
            Subject = p('td')[6].string
            URL = p('td')[7]('a')[0].attrs['href'][86:]
            InspectionReports[ID] = {'Date': Date, 'School Roll No.': SchoolRoll, 'County': County, 'School Name': SchoolName, 'School Level': SchoolLevel, 'Inspection Type': InspectionType, 'Subject': Subject, 'URL': URL}
            ID = ID + 1

    df_InspectionReports = pd.DataFrame.from_dict(InspectionReports, orient='index')
    General_InspectionReports = pd.concat([General_InspectionReports,df_InspectionReports])

print(f"Number of reports to download: {len(General_InspectionReports)}")

# Download PDF
PDFToConvert = []
for index, row in General_InspectionReports.iterrows():
    DownloadURL = 'https://www.education.ie/en/Publications/Inspection-Reports-Publications/Whole-School-Evaluation-Reports-List/' + row['URL']
    FileName = 'Reports/pdf/' + row['School Roll No.'] + '_' + row['Date'] + '.pdf'
    PDFToConvert.append('Reports/pdf/' + row['School Roll No.'] + '_' + row['Date'])
    print('\tReport ' + row['School Roll No.'] + ' downloaded')
    wget.download(DownloadURL, FileName)

# Converte PDF to text and remove useless data
print("\nProcessing data...")

if os.path.exists(PATH_TO_TEXT_REPORTS) == False:
    os.mkdir(PATH_TO_TEXT_REPORTS)

ConvertionCategories = {"Properly processed":0, "Not in text format":0, "Cannot be processed":0}
FilesProperlyConverted = {}
FilesNotConverted = []

for PDF in PDFToConvert:
    try:
        extracted_report = extract_text(f"{PDF}.pdf")
        if "ú" in extracted_report :
            FilesNotConverted.append(PDF[len('Reports/pdf/'):])
            continue
        with open(f"{PATH_TO_TEXT_REPORTS}/{PDF[len('Reports/pdf/'):]}.txt" ,"w+") as f:
            f.write(extracted_report)
    except (KeyError, UnicodeEncodeError):
        ConvertionCategories["Cannot be processed"] = ConvertionCategories["Cannot be processed"] + 1
        FilesNotConverted.append(PDF[len('Reports/pdf/'):])
        print(PDF[len('Reports/pdf/'):] + ' could not be processed')
        continue


print("Data sucessfuly processed !")
print(f"Number of errors during process: {len(FilesNotConverted)}\t{len(FilesNotConverted) / len(General_InspectionReports) * 100}%")