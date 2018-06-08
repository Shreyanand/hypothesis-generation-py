#Importing configuration
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("config.txt")

word2vec_path = config.get("configuration","word2vec_path")

# Importing word2vec to find similarity and neighboring words
import gensim
from gensim.models import Word2Vec

model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_path, binary=True) 

#sentence = "ISIL members threw stones in Paris."

topk = 10

print(model.most_similar(['ISIL'], [], topk))
print(model.most_similar('threw_stones', [], topk))
print(model.most_similar(['Paris'], [], topk))
