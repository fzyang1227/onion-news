import re
import contractions
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
stopwords = nltk.corpus.stopwords.words('english')

def process_text(text):
    ''' process the text of a document
    args.
        text: a string
    returns.
        Counter object with word counts
    '''
    # remove line breaks
    text.replace('\n', ' ')
    
    # expand contractions
    expanded = ' '.join([contractions.fix(word) for word in text.split()])
    
    # remove punctuation and numbers
    expanded.replace('-', ' ') # replace hyphens with spaces
    expanded = re.sub(r'[^\w\s]', '', expanded)
    expanded = re.sub(r'\d+', '', expanded)
    
    # extract not proper nouns
    other_words = ' '.join([word for word, pos in pos_tag(expanded.split()) if pos != 'NNP' and pos !='NNPS'])

    # lowercase, remove stopwords, and stem words
    other_words = [word for word in other_words.lower().split() if word not in stopwords]
    lemma = WordNetLemmatizer()
    words = ' '.join([lemma.lemmatize(word) for word in other_words])
    
    return words