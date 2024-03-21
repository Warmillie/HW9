from mongoengine import connect
import json
from models import Author, Quote
from bson import ObjectId
from mongoengine import connect
from models import Quote

def search_quotes(criteria):
    if criteria.startswith("name:"):
        author_name = criteria.split(":", 1)[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            if quotes:
                for quote in quotes:
                    print(f"Author: {quote.author.fullname}")
                    print(f"Quote: {quote.text}")
                    print(f"Tags: {', '.join(quote.tags)}")
                    print()
            else:
                print("No quotes found for the author:", author_name)
        else:
            print("No author found with name:", author_name)
    elif criteria.startswith("tag:"):
        tag = criteria.split(":", 1)[1].strip()
        quotes = Quote.objects(tags__icontains=tag)
        if quotes:
            for quote in quotes:
                print(f"Author: {quote.author.fullname}")
                print(f"Quote: {quote.text}")
                print(f"Tags: {', '.join(quote.tags)}")
                print()
        else:
            print("No quotes found with tag:", tag)
    elif criteria.startswith("tags:"):
        tags = criteria.split(":", 1)[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        if quotes:
            for quote in quotes:
                print(f"Author: {quote.author.fullname}")
                print(f"Quote: {quote.text}")
                print(f"Tags: {', '.join(quote.tags)}")
                print()
        else:
            print("No quotes found with tags:", ', '.join(tags))
    else:
        print("Invalid search criteria. Please use 'name:', 'tag:' or 'tags:'")


if __name__ == "__main__":
    connect(host='mongodb+srv://warmillie1:%23EDCxsw2!QAZ@cluster0.ezi9yvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

    while True:
        command = input("Enter search criteria (name:<author_name>, tag:<tag>, tags:<tag1>,<tag2>,...): ")
        if command.lower() == "exit":
            break
        search_quotes(command)

