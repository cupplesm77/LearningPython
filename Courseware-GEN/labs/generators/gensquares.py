# gensquares.py

def gen_squares(max_root):
    root = 0
    while root <= max_root:
        yield root ** 2
        root += 1


squares = gen_squares(5)
# for square in squares:
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# print(next(squares))

# returns 42
nums = gen_squares(1)
print(next(nums, 33))
print(next(nums, 33))
print(next(nums, 33))


def myitems(top):
    for x in range(top, 0, -1):
        yield top ** 2
        top -= 1
    yield "All done."


num = 1
for item in myitems(num):
    print(item)


# Tokenizing
# Produce the tokens/words in a string, one at a time.
# Immediately stop producing tokens when the tokenizer encounters the word "EOF".

def tokens(text):
    start = 0
    end = body.find(" ", start)
    while end > 0:
        token = text[start:end]
        if token == "EOF":
            return
        yield token
        start = end + 1
        end = text.find(" ", end + 1)
    yield text[start:]


body = "int main() { return 0; } EOF More Text"
for tks in tokens(body):
    print(tks)
