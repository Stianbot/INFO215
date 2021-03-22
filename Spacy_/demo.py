import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import date


def get_paragraphs(list_of_urls):
    p = ""
    for url in list_of_urls:
        bs = BeautifulSoup(urlopen(url), 'html.parser')
        for paragraph in bs.find_all('p'):
            p += paragraph.get_text()
    return p


def tokenize(nlp_obj):
    stopwords = list(STOP_WORDS)
    acceptable_word_types = ['PROPN', 'ADJ', 'NOUN', 'VERB']
    words = []

    for token in nlp_obj:
        if token.text in stopwords or token.text in punctuation:
            continue

        if token.pos_ in acceptable_word_types:
            words.append(token.text)
    return words


def weigh_words(list_of_words):
    frequency = Counter(list_of_words)
    max_freq = Counter(list_of_words).most_common(5)[0][1]

    for word in frequency.keys():
        frequency[word] = (frequency[word] / max_freq)
    return frequency


def weigh_sentences(weighted_words, doc):
    sentence_strength = {}

    for sentence in doc.sents:
        for word in sentence:
            if word.text in weighted_words.keys():
                if sentence in sentence_strength.keys():
                    sentence_strength[sentence] += weighted_words[word.text]
                else:
                    sentence_strength[sentence] = weighted_words[word.text]

    return sentence_strength


def make_summary(sentence_strength, n_sentences):
    summarized_sentences = nlargest(n_sentences, sentence_strength, key=sentence_strength.get)
    final_sentences = [w.text for w in summarized_sentences]
    summary = "\n".join(final_sentences)
    return summary


def generate_references(ref_list):
    text = ""
    for ref in enumerate(ref_list):
        text += f"[{ref[0] + 1}]: {ref[1]}. "

    text += f"(accessed: {date.today().strftime('%B %d, %Y')})"
    return text


def program():

    list_of_webpages = ["https://en.wikipedia.org/wiki/Web_scraping",
                        "https://en.wikipedia.org/wiki/Data_scraping"]

    all_p = get_paragraphs(list_of_webpages)
    nlp = spacy.load('en_core_web_sm')
    document = nlp(all_p)
    tokenized_words = tokenize(document)
    weighted_words = weigh_words(tokenized_words)
    weighted_sentences = weigh_sentences(weighted_words, document)
    summary = make_summary(weighted_sentences, 10)
    references = generate_references(list_of_webpages)
    turn_in = f"{summary}\n----------\nWord count: {len(summary.split())}.\nReferences: {references}"

    f = open("oblig4.txt", "w")
    f.write(turn_in)

program()
