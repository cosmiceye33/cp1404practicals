
import wikipedia

choice = input("Page: ")
while choice != "":
    wikipedia.search(choice)
    searched_page = wikipedia.page(choice)
    print(searched_page.title())
    print(searched_page.url())
    try:
        print(wikipedia.summary(searched_page, sentences=1))
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Did you mean: ? {e.options}")
    searched_page = input("Page: ")

