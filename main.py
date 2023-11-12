import random
import long_arrays
import arrays as a
###Simple Script to help the players creativity in the character creation of Dungeons and Dragons###

print("Hey there adventurer! I'm the keeper of Earia's library where the history of the past, present and future is found.\n"
      "I see you are looking for a book, the amount of books in here is near infinite. All across the multiverse different books\n"
      "appear in our shelves by the minute, what about some extra information like who's the book about?")

name = input("Insert a name: ")

print(f"Oh! {name}, thats an interesting one, oh I can't wait!")

print(f"{name}, {a.titulo} of {a.city} was a {long_arrays.desc} capable of many feats.\n"
      f"Curious enough {a.pronoun} has an ever changing story, almost as if someone or something was temepring with fate.\n"
      f"According to stories {a.pronoun} {long_arrays.tragedy} Such a {a.tragedy_r}.\n"
      f"No wonder {name} became a {a.pclass}.")
print("Come back to the library whenever you need a new book, i'm lonely in here.")