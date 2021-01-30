import pandas as pd
import os
import re

REPO = "plain_text"
parsed = []

for session_file in os.listdir(REPO):
    filepath = os.path.join(REPO, session_file)

    f = open(filepath)
    data = f.read()
    parsed += re.findall("School name .+?(?= School| Seoladh)", data)
    parsed += re.findall("School address .+?(?= Uimhir| Roll)", data)
    parsed += re.findall("Roll number .+?(?= Date)", data)
    parsed += re.findall("Date of inspection|Evaluation: .+?(?= )", data)

print(parsed)