import pandas as pd
import os
import re

REPO = "Reports/plain_text"
parsed = []

def isNan (_str):
    if not _str:
        return ["Nan"]
    else:
        return _str

for session_file in os.listdir(REPO):
    filepath = os.path.join(REPO, session_file)

    f = open(filepath)
    data = f.read()
    line = []
    line += isNan(re.findall("School name .+?(?= School| Seoladh)", data))
    line += isNan(re.findall("School address .+?(?= Uimhir| Roll)", data))
    line += isNan(re.findall("Roll number .+?(?= Date)", data))
    line += isNan(re.findall("Date of (?:Evaluation:|inspection:) .+?(?= )", data))
    parsed.append(line)

for line in parsed:
    print(line)