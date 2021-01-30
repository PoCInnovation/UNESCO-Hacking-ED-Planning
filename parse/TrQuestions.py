import numpy as np

from transformers import pipeline
from metaData import getInfo

nlp_qa = pipeline('question-answering')

def getQnA(path: str):
    """
    Ask basics questions to the model with respect to the given context

    Parameters:
    path: path to context file

    Returns:
    array: result for all of the nith questions
    """
    result = []

    to_summ = getInfo(path)
    result.append(nlp_qa(context=to_summ[0], question='What is the school name')['answer'])
    result.append(nlp_qa(context=to_summ[1], question='What is the school address')['answer'])
    result.append(nlp_qa(context=to_summ[2], question='What is the roll number')['answer'])
    result.append(nlp_qa(context=to_summ[3], question='What is the date of evaluation')['answer'])
    result.append(nlp_qa(context=to_summ[4], question='What is the quality of pupils')['answer'])
    result.append(nlp_qa(context=to_summ[5], question='What is the quality of teaching')['answer'])
    result.append(nlp_qa(context=to_summ[6], question='What is the quality of support')['answer'])
    result.append(nlp_qa(context=to_summ[7], question='What is the quality of leadership')['answer'])
    result.append(nlp_qa(context=to_summ[8], question='What is the quality of school')['answer'])
    return result

if __name__ == "__main__":
    result = getQnA("../Reports/plain_text/01421F_16_05_2019.txt")
    [print(info) for info in result]