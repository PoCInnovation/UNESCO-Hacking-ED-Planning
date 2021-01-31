import pandas as pd
import os
import re
import sys

def isNan (_str):
    return _str if _str else ["NaN"]


def getSchoolName(text: str):
    name = re.sub(r'\W+ ', '', isNan(re.findall("School name (.+?)(?= School| Seoladh)", text))[0])
    if name == 'NaN': name = re.sub(r'\W+ ', '', isNan(re.findall("\n(.+?)\n.+?\nRoll", text))[0])
    if name == 'NaN': name = re.sub(r'\W+ ', '', isNan(re.findall("\n(.+?)\n.+?\nUimhir rolla:", text))[0])
    if name == 'NaN': name = re.sub(r'\W+ ', '', isNan(re.findall("School address \n\n(.+?) /", text))[0])
    # School address
    return name


def getSchoolAddress(text: str):
    addr = re.sub(r'\W+ ', '', isNan(re.findall("School address (.+?)(?= Uimhir| Roll)", text))[0])
    if addr == 'NaN': addr = re.sub(r'\W+ ', '', isNan(re.findall("Virginia, County Cavan", text))[0])
    if addr == 'NaN': addr = re.sub(r'\W+ ', '', isNan(re.findall("\n(.+?)\nRoll", text))[0])
    if addr == 'NaN': addr = re.sub(r'\W+ ', '', isNan(re.findall("\n(.+?)\nUimhir rolla", text))[0])
    return addr


def getRollNumber(text: str):
    roll = re.sub(r'\W+ ', '', isNan(re.findall("Roll number  (.+?)(?= Date)", text))[0])
    if roll == 'NaN': roll = re.sub(r'\W+ ', '', isNan(re.findall("Roll number: (.+?)(?= Date)", text))[0])
    if roll == 'NaN': roll = re.sub(r'\W+ ', '', isNan(re.findall("Roll number: (.+?)\n", text))[0])
    if roll == 'NaN': roll = re.sub(r'\W+ ', '', isNan(re.findall("Uimhir rolla:  (.+?)\n", text))[0])
    return roll


def getInspactionDate(text: str):
    date = re.sub(r'\W+ ', '', isNan(re.findall("Date of (?:Evaluation:|inspection:) (.+?)(?= )", text, flags=re.IGNORECASE))[0])
    if date == 'NaN': date = re.sub(r'\W+ ', '', isNan(re.findall("Date of inspection:(.+?)", text, flags=re.IGNORECASE))[0])
    if date == 'NaN': date = re.sub(r'\W+ ', '', isNan(re.findall("Date of Inspection (.+?)", text, flags=re.IGNORECASE))[0])
    return date


def getPupilsQuality(text: str):
    four = re.sub(r'\W+  ', '', isNan(re.findall("(?:THE QUALITY OF PUPILS’|the quality of pupils’ ).+?(?=[0-9])", text, flags=re.IGNORECASE))[0])
    if four == 'NaN': four = re.sub(r'\W+  ', '', isNan(re.findall("The learning achievements of pupils.+?\d", text, flags=re.IGNORECASE|re.DOTALL))[0])
    return four


def getTeachingQuality(text: str):
    five = re.sub(r'\W+  ', '', isNan(re.findall("(?:THE QUALITY OF TEACHING|the quality of teaching ).+?(?=[0-9])", text, re.IGNORECASE))[0])
    if five == 'NaN': five = re.sub(r'\W+  ', '', isNan(re.findall("(QUALITY OF LEARNING AND TEACHING.+?)IMPLEMENTATION OF RECOMMENDATION", text, flags=re.IGNORECASE|re.DOTALL))[0])
    return five


def getLeadershipQuality(text: str):
    seven = re.sub(r'\W+  ', '', isNan(re.findall("(?:THE QUALITY OF LEADERSHIP|the quality of LEADERSHIP ).+?(?=[0-9])", text, re.IGNORECASE))[0])
    if seven == 'NaN': seven = re.sub(r'\W+  ', '', isNan(re.findall("(QUALITY OF SCHOOL MANAGEMENT AND LEADERSHIP.+?)QUALITY OF LEARNING AND TEACHING", text, flags=re.IGNORECASE|re.DOTALL))[0])
    return seven


def getInfo(path):
    f = open(path)
    data = f.read()
    line = []

    data = re.sub("The Inspectorate’s Quality Continuum.+?(?= difficulties)", '', data)
    data = re.sub("THE INSPECTORATE’S QUALITY CONTINUUM.+?(?= difficulties)", '', data)

    line.append(getSchoolName(data))
    line.append(getSchoolAddress(data))
    line.append(getRollNumber(data))
    line.append(getInspactionDate(data))
    line.append(getPupilsQuality(data))
    line.append(getTeachingQuality(data))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF SUPPORT|the quality of support ).+?(?=[0-9])", data))[0]))
    line.append(getLeadershipQuality(data))
    line.append(re.sub(r'\W+ ', '', isNan(re.findall("(?:THE QUALITY OF SCHOOL|the quality of school ).+?(?=[0-9])", data))[0]))
    return (line)


if __name__ == '__main__':
    res = []
    for f in os.listdir("../Reports/plain_text/"):
        res.append(getInfo("../Reports/plain_text/" + f))
    missing = 0
    for r in res:
        if r[5] == 'NaN':
            missing += 1
    print("Success rate:", 100 - missing / len(res) * 100)