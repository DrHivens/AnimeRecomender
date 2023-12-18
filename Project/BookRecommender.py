import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class BookRecommender:

	def __init__(self, dataframe):
		self.df = dataframe
		self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
		self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.df['Summary'])
		self.indices = pd.Series(self.df.index, index=self.df['Title']).drop_duplicates()

	def get_recommendations(self, title, top_n=5):

		# Get the index of the book that matches the title
		idx = self.indices[title]

		# Compute the cosine similarity matrix
		cosine_similarities = linear_kernel(self.tfidf_matrix[idx], self.tfidf_matrix).flatten()

		# Get the most similar books
		related_books_indices = cosine_similarities.argsort()[:-top_n-1:-1]

		# Return the top n most similar books
		return self.df['Title'].iloc[related_books_indices]

