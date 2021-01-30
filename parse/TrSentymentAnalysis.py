from transformers import pipeline

nlp_sentence_classif = pipeline('sentiment-analysis')

def getSentiment(text: str) -> str:
    """
    Analyse sentiment of the given text

    Parameters:
    path: text to analyse

    Returns:
    Sentiment: Sentiment containing score, start, end and label
    """
    return nlp_sentence_classif(text)

if __name__ == "__main__":
    print(getSentiment("Such a nice hackathon !"))