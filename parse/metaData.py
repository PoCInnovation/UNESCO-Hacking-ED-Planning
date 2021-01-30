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

    line += isNan(re.findall("School name .+?(?= School| Seoladh)", data))
    line += isNan(re.findall("School address .+?(?= Uimhir| Roll)", data))
    line += isNan(re.findall("Roll number .+?(?= Date)", data))
    line += isNan(re.findall("Date of (?:Evaluation:|inspection:) .+?(?= )", data))
    line += isNan(re.findall("(?:THE QUALITY OF PUPILS’|the quality of pupils’ ).+?(?=[0-9])", data))
    line += isNan(re.findall("(?:THE QUALITY OF TEACHING|the quality of teaching ).+?(?=[0-9])", data))
    line += isNan(re.findall("(?:THE QUALITY OF SUPPORT|the quality of support ).+?(?=[0-9])", data))
    line += isNan(re.findall("(?:THE QUALITY OF LEADERSHIP|the quality of LEADERSHIP ).+?(?=[0-9])", data))
    line += isNan(re.findall("(?:THE QUALITY OF SCHOOL|the quality of school ).+?(?=[0-9])", data))
    return (line)



#for session_file in os.listdir(REPO):
#    filepath = os.path.join(REPO, session_file)
#
#    f = open(filepath)
#    data = f.read()
#    line = []
#    line += isNan(re.findall("School name .+?(?= School| Seoladh)", data))
#    line += isNan(re.findall("School address .+?(?= Uimhir| Roll)", data))
#    line += isNan(re.findall("Roll number .+?(?= Date)", data))
#    line += isNan(re.findall("Date of (?:Evaluation:|inspection:) .+?(?= )", data))
#    line += isNan(re.findall("(?:THE QUALITY OF PUPILS’|the quality of pupils’ ).+?(?=[0-9])", data))
#    line += isNan(re.findall("(?:THE QUALITY OF TEACHING|the quality of teaching ).+?(?=[0-9])", data))
#    line += isNan(re.findall("(?:THE QUALITY OF SUPPORT|the quality of support ).+?(?=[0-9])", data))
#    line += isNan(re.findall("(?:THE QUALITY OF LEADERSHIP|the quality of LEADERSHIP ).+?(?=[0-9])", data))
#    line += isNan(re.findall("(?:THE QUALITY OF SCHOOL|the quality of school ).+?(?=[0-9])", data))
#    parsed.append(line)
#
#for line in parsed:
#    print(line)

if __name__ == '__main__':
    print (getInfo("../Reports/plain_text/13299E_13_01_2021.txt")[4])