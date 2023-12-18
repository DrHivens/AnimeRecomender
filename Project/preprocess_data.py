import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.data import find


def init():
	download_nltk_resources()
	pd.set_option('display.max_columns', 1000)


def end():
	pd.reset_option('display.max_colwidth')


def download_nltk_resources():
	try:
		find('tokenizers/punkt')
	except LookupError:
		nltk.download('punkt')


def print_full_dataframe(df):
	with pd.option_context('display.max_colwidth', 1000):
		print(df)


def preprocess_data(data):
	init()
	df = pd.DataFrame(data, columns=['Title', 'Authors', 'Summary'])
	df = df.drop_duplicates(subset='Title', keep='first')
	df.fillna("Information non disponible.", inplace=True)
	df['Summary'] = df['Summary'].astype(str)
	df['Tokens'] = df['Summary'].apply(word_tokenize)
	print("Les Donneés:" + str(df.head()))
	end()
	return df
