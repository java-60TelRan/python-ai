from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy

class TextModel:
    def __init__(self, text: str):
        text_arr = text.split('.')
        self.text_model = [res for s in text_arr if (res := s.strip())]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.embeddings_text = self.vectorizer.fit_transform(self.text_model)
    def getAnswers(self, query: str, nAnswers: int) -> list[str]:
        res = []
        if self.getKnownWords(query):
            embeddings_query = self.vectorizer.transform([query])
            
            sims:numpy = cosine_similarity(self.embeddings_text, embeddings_query)
            simsFlat = sims.ravel()
            indices = numpy.argsort(simsFlat)[::-1]  # reverse order
            res =  [self.text_model[i] for i in indices[:nAnswers] if simsFlat[i]]
        return res
    def getKnownWords(self, answer:str)->set[str]:
        answerWords: set[str] = set(answer.lower().split())
        knownWords: set[str] = self.vectorizer.vocabulary_.keys()
        return answerWords & knownWords
        
        
  