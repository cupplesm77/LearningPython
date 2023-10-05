# misc.py

# count the number of sentences in a simple sentence
text = """This is a longer story.

Once upon a time, there was a princess in a castle.

She grew up to be a famous dancer."""

print(f"string = {text}")
print("")

text_replace = text.replace("\n", " ")
print(f"string with new-lines removed = {text_replace}")

text_count_sentences = 1 + text_replace.count(". ")
print(f"number of sentences in text_replace = {text_count_sentences}")
