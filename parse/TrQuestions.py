import numpy as np

from transformers import pipeline
from metaData import getInfo

nlp_qa = pipeline('question-answering')

def getQnA(path: str, from_text=False):
    """
    Ask basics questions to the model with respect to the given context

    Parameters:
    path: path to context file

    Returns:
    array: result for all of the nith questions
    """
    result = []
    context = ""

    context = getInfo(path) if from_text == False else path
    result.append({'question': 'What is the school name',           'result': nlp_qa(context=context[0], question='What is the school name')})
    result.append({'question': 'What is the school address',        'result': nlp_qa(context=context[1], question='What is the school address')})
    result.append({'question': 'What is the roll number',           'result': {'score': 1, 'answer': context[2]}})
    result.append({'question': 'What is the date of evaluation',    'result': nlp_qa(context=context[3], question='What is the date of evaluation')})
    result.append({'question': 'What is the quality of pupils',     'result': nlp_qa(context=context[4], question='What is the quality of pupils')})
    result.append({'question': 'What is the quality of teaching',   'result': nlp_qa(context=context[5], question='What is the quality of teaching')})
    result.append({'question': 'What is the quality of support',    'result': nlp_qa(context=context[6], question='What is the quality of support')})
    result.append({'question': 'What is the quality of leadership', 'result': nlp_qa(context=context[7], question='What is the quality of leadership')})
    result.append({'question': 'What is the quality of school',     'result': nlp_qa(context=context[8], question='What is the quality of school')})
    return result

if __name__ == "__main__":
    result = getQnA("../Reports/plain_text/01421F_16_05_2019.txt")
    [print(info) for info in result]