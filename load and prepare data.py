nltk.download('movie_reviews')
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# Prepare text and labels
texts = [" ".join(words) for words, label in documents]
labels = [label for words, label in documents]
