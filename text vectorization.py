vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)
