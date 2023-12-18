import data_collector
import data_collector2
from env import DOWNLOADED_BOOKS_FILE_NAME, BOOKS_FILE_NAME, BOOKS_LENGTH
from preprocess_data import preprocess_data, print_full_dataframe
from user_interface import user_interface
downloaded_books = None
books = None


def fetch_books():
	print("Téléchargement des livres...")
	global downloaded_books
	downloaded_books = data_collector.fetch_books_from_open_library(query="science fiction",  num_books=BOOKS_LENGTH)
	downloaded_books = data_collector2.fetch_books_from_open_library2(query="science fiction", num_books=2)
	# data_collector.save_books_to_csv(downloaded_books, filename=DOWNLOADED_BOOKS_FILE_NAME)


def process_books():
	print("Prétraitement des livres...")
	global books, downloaded_books
	books = preprocess_data(downloaded_books)
	books.to_csv(BOOKS_FILE_NAME, index=False)
	print_full_dataframe(books.head())


def start_recommendations():
	user_interface()


def main():
	fetch_books()
	process_books()
	start_recommendations()


if __name__ == "__main__":
	main()
