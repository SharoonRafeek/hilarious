import spacy
import en_core_web_lg

nlp = en_core_web_lg.load()


def keywords(joke):
    doc = nlp(joke)
    keywords = doc.ents

    return keywords
