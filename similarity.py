# Importing word2vec to find similarity and neighboring words
import gensim
from gensim.models import Word2Vec

model = gensim.models.KeyedVectors.load_word2vec_format('~/word2vec-model/GoogleNews-vectors-negative300.bin', binary=True) 

#sentence = "ISIL members threw stones in Paris."

topk = 3 

print(model.most_similar(['ISIL', 'organisation'], [], topk))

print(model.most_similar('threw_stones', [], topk))

print(model.most_similar(['Paris', 'city'], [], topk))
