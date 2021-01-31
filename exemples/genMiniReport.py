import numpy as np
from transformers import pipeline
from fpdf import FPDF
import metaData
import dataExtraction

nlp_sum = pipeline('summarization')

class PDF(FPDF):
    def lines(self):
        self.set_fill_color(32.0, 47.0, 250.0) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255, 255, 255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0,'FD')

    def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="UNESCO Mini Report", border=0)

    def addText(self, x, y, w, h, text, align):
        self.set_xy(x, y)
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(w , h, align=align, txt=text)

    def _repr_latex_(self):
        return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)

def getMiniReport(infos):
    """
    Generate a mini report from a bigger One

    Parameters:
    path: path to context file

    Returns:
    array: the location of the new PDF
    """
    result = []

    result.append(infos[0])
    result.append(infos[1])
    result.append(infos[2])
    result.append(infos[3])
    result.append(nlp_sum(infos[4]))
    result.append(nlp_sum(infos[5]))
    # result.append(nlp_qa(context=to_summ[5], question='What is the quality of teaching')['answer'])
    # result.append(nlp_qa(context=to_summ[6], question='What is the quality of support')['answer'])
    # result.append(nlp_qa(context=to_summ[7], question='What is the quality of leadership')['answer'])
    # result.append(nlp_qa(context=to_summ[8], question='What is the quality of school')['answer'])

    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.titles()

    pdf.addText(10, 30, 0, 6, "School Name:\n" + result[0], 'C')
    pdf.addText(10, 45, 0, 6, "School Adress:\n" + result[1], 'C')
    pdf.addText(10, 60, 0, 6, "School Roll:\n" + result[2], 'C')
    pdf.addText(10, 70, 0, 6, "Evaluation Date:\n" + result[3], 'C')

    print(result[4][0]['summary_text'])

    pdf.addText(0, 90, 0, 10, "I - Quality Of Pupils", 'L')
    pdf.addText(0, 100, 0, 10, result[4][0]['summary_text'], 'L')

    pdf.addText(0, 120, 0, 10, "II - Quality Of Teaching", 'L')
    pdf.addText(0, 110, 0, 10, result[5][0]['summary_text'], 'L')

    pdf.output('test.pdf','F')
    return pdf

if __name__ == "__main__":
    report = dataExtraction.PDFToText("exemple_report.pdf")
    reportInfos = metaData.getInfo(report, from_text=True)
    result = getMiniReport(reportInfos)
    [print(info) for info in result]