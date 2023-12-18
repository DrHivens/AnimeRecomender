import csv
import requests
from env import BASE_URL


def fetch_books_from_open_library(query="science fiction", num_books=100):
    books = []
    page = 1
    print(f"Téléchargement des livres avec la requête '{query}'...")
    while len(books) < num_books:
        print(f"Téléchargement de la page {page}...")
        params = {
            "q": query,
            "limit": min(100, num_books - len(books)),
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            results = response.json()
            print(f"Nombre de livres téléchargés: {len(results.get('docs', []))}")
            printt = True
            for doc in results.get("docs", []):
                title = doc.get("title_suggest", "Titre inconnu")
                authors = ", ".join(doc.get("author_name", ["Auteur inconnu"]))
                edition_key = doc.get("first_publish_year", "Information non disponible.")
                books.append([title, authors, edition_key])
                if len(books) >= num_books:
                    break
        else:
            break
        page += 1
    print(f"{len(books)} livres téléchargés.")
    return books


def save_books_to_csv(books, filename="books_data.csv"):
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Authors", "First Publish Year"])
        writer.writerows(books)
    print(f"{len(books)} livres sauvegardés dans {filename}")
