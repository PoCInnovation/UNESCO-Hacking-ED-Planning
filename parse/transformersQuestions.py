import re
import numpy as np
import sys

from transformers import pipeline
from metaData import getInfo

to_summ = getInfo("../Reports/plain_text/01421F_16_05_2019.txt") # student achiv == [4]

nlp_qa = pipeline('question-answering')

print(f"What is the school name\t: {nlp_qa(context=to_summ[0],        question='What is the school name')['answer']}")
print(f"What is the school address\t: {nlp_qa(context=to_summ[1],     question='What is the school address')['answer']}")
print(f"What is the roll number\t: {nlp_qa(context=to_summ[2],        question='What is the roll number')['answer']}")
print(f"What is the date of evaluation\t: {nlp_qa(context=to_summ[3], question='What is the date of evaluation')['answer']}")
print(f"Quality of pupils\t: {nlp_qa(context=to_summ[4],              question='What is the quality of pupils')['answer']}")
print(f"Quality of teaching\t: {nlp_qa(context=to_summ[5],            question='What is the quality of teaching')['answer']}")
print(f"Quality of support\t: {nlp_qa(context=to_summ[6],             question='What is the quality of support')['answer']}")
print(f"Quality of leadership\t: {nlp_qa(context=to_summ[7],          question='What is the quality of leadership')['answer']}")
print(f"Quality of school\t: {nlp_qa(context=to_summ[8],              question='What is the quality of school')['answer']}")