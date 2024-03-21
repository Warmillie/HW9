import json
from models import Author, Quote



def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_authors():
    authors_data = load_data_from_json('authors.json')
    for author_data in authors_data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()

def load_quotes():
    quotes_data = load_data_from_json('quotes.json')
    for quote_data in quotes_data:
        author_fullname = quote_data['author']
        author = Author.objects(fullname=author_fullname).first()
        if author:
            quote = Quote(
                author=author,
                text=quote_data['quote'],
                tags=quote_data['tags']
            )
            quote.save()
        else:
            print("No author found with fullname:", author_fullname)

if __name__ == '__main__':
    load_authors()
    load_quotes()
    print('Дані завантажено успішно.')
