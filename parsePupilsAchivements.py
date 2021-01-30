import os
import re
import pandas as pd

REPO = "Reports/plain_text"
parsed = []
for session_file in os.listdir(REPO):
    filepath = os.path.join(REPO, session_file)

    f = open(filepath)
    data = f.read()
    regex1 = re.findall("Learningand Pupil Achievement...(.+?).\d", data)
    if (len(regex1) == 0):
        parsed.append(re.findall("LEARNING ACHIEVEMENTS OF PUPILS...(.+?).\d", data))
    else:
        parsed.append(regex1)

r = 0
for i in range(len(parsed)):
    if len(parsed[i]) == 0:
        r += 1

print(f"Result: {(r / len(parsed) * 100):.2f}%")
