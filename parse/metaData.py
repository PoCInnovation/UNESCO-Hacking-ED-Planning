import pandas as pd
import os
import re

REPO = "plain_text"
parsed = []

for session_file in os.listdir(REPO):
    filepath = os.path.join(REPO, session_file)

    f = open(filepath)
    data = f.read()
    line = []
    line += re.findall("School name .+?(?= School| Seoladh)", data)
    line += re.findall("School address .+?(?= Uimhir| Roll)", data)
    line += re.findall("Roll number .+?(?= Date)", data)
    line += re.findall("Date of (?:Evaluation:|inspection:) .+?(?= )", data)
    parsed.append(line)

for line in parsed:
    print(line)