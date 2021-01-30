import os
import re
import pandas as pd

REPO = "Reports/plain_text"
parsed = []
for session_file in os.listdir(REPO):
    filepath = os.path.join(REPO, session_file)

    f = open(filepath)
    data = f.read()
    regex = []
    regex = re.findall("Quality of Teaching, Learning and Pupil Achievement[\s\S][\w\W]+?\d", data, flags=re.IGNORECASE)
    if (len(regex) == 0): regex = re.findall("(?:THE QUALITY OF PUPILS’|the quality of pupils’ ).+?(?=[0-9])", data, flags=re.IGNORECASE)
    if (len(regex) == 0): regex = re.findall("Quality of Teaching, Learning and Pupil Achievement[\s\S][\w\W]+?\d", data, flags=re.IGNORECASE)
    if (len(regex) == 0): regex = re.findall("The quality of learning and teaching[\s\S][\w\W]+?\d", data, flags=re.IGNORECASE)
    if (len(regex) == 0): regex = re.findall("LEARNING ACHIEVEMENTS OF PUPILS[\s\S][\w\W]+?(.+?).\d", data, flags=re.IGNORECASE)
    if (len(regex) == 0): regex = re.findall("QUALITY OF TEACHING AND LEARNING[\s\S][\w\W]+?(.+?).\d", data, flags=re.IGNORECASE)
    if (len(regex) == 0): print("Reports/pdf/" + filepath[len("Reports/plain_text/"):-4] + ".pdf")
    parsed.append(regex)

r = 0
for i in range(len(parsed)):
    if len(parsed[i]) == 0:
        r += 1

print(f"Success rate: {(100 - (r / len(parsed) * 100)):.2f}%")