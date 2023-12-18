import pandas as pd

from BookRecommender import BookRecommender
from env import BOOKS_FILE_NAME


def user_interface():
	print("\nSystème de Recommandation de Livres")
	print("-----------------------------------")
	books = pd.read_csv(BOOKS_FILE_NAME)
	recommender = BookRecommender(books)
	while True:
		print("\nMenu:")
		print("1. Obtenir des recommandations de livres")
		print("2. Quitter")
		choice = input("Choisissez une option (1/2): ")
		if choice == '1':
			book_title = input("\nEntrez le titre du livre pour obtenir des recommandations (ex: Herland Illustrated): ")
			try:
				recommendations = recommender.get_recommendations(book_title)
				print(recommendations)
				print("\nLivres recommandés pour '{}':".format(book_title))
				for idx, title, summary in enumerate(recommendations, 1):
					for t in title:
						print("t:" + t)
					for s in summary:
						print("s:" + s)
					print("{}. {}".format(idx, title))
			except KeyError:
				print("\nDésolé, ce titre n'est pas dans notre base de données. Veuillez essayer un autre titre.")
		elif choice == '2':
			print("\nMerci d'avoir utilisé notre système de recommandation. À bientôt!")
			break
		else:
			print("\nOption invalide. Veuillez choisir une option valide.")
