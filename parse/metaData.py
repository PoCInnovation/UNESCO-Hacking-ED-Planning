import pandas as pd
import os
import re
import sys

def isNan (_str):
    return _str if _str else ["NaN"]

def getInfo (path):
    f = open(path)
    data = f.read()
    line = []

    data = re.sub("The Inspectorate’s Quality Continuum.+?(?= difficulties)", '', data)
    data = re.sub("THE INSPECTORATE’S QUALITY CONTINUUM.+?(?= difficulties)", '', data)

    line.append(re.sub(r'\W+ ', '', isNan(re.findall("School name .+?(?= School| Seoladh)", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("School address .+?(?= Uimhir| Roll)", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("Roll number .+?(?= Date)", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("Date of (?:Evaluation:|inspection:) .+?(?= )", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF PUPILS’|the quality of pupils’ ).+?(?=[0-9])", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF TEACHING|the quality of teaching ).+?(?=[0-9])", data))[0]))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF SUPPORT|the quality of support ).+?(?=[0-9])", data))[0]))
    seven = re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF LEADERSHIP|the quality of LEADERSHIP ).+?(?=[0-9])", data, re.IGNORECASE))[0])
    if seven == 'NaN': seven = re.sub(r'\W+ ', '', isNan(re.findall("(QUALITY OF SCHOOL MANAGEMENT AND LEADERSHIP.+?)QUALITY OF LEARNING AND TEACHING", data, flags=re.IGNORECASE|re.DOTALL))[0])
    line.append(seven)
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF SCHOOL|the quality of school ).+?(?=[0-9])", data))[0]))
    return (line)
    # if line[7] == 'NaN':
    #     print("../Reports/pdf/" + path[len("../Reports/plain_text/"):-len(".txt")] + ".pdf")
    #     exit()
    # return (line)


if __name__ == '__main__':
    res = []
    for f in os.listdir("../Reports/plain_text/"):
        res.append(getInfo("../Reports/plain_text/" + f))
    missing = 0
    for r in res:
        if r[7] == 'NaN':
            missing += 1
    print("Success rate:", 100 - missing / len(res) * 100)
    # print (getInfo("../Reports/plain_text/13299E_13_01_2021.txt")[4])