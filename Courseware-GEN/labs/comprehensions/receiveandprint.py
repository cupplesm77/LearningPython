# receiveandprint.py

def receive_and_print():
    print('Starting...')
    try:
        while True:
            payload = (yield)
            print("RECEIVED: " + payload)
    except GeneratorExit:
        print("CLOSING")
        # 'raise' is optional in this case, bacause the next line will
        # exit the function anyway.  But for other gen functions, you
        # might need it.
        raise


reciever = receive_and_print()
next(reciever)
reciever.send("Python")
reciever.send("Rocks")
reciever.close()
reciever.send("one more")

print("")
colors = ['aquamarine', 'orange', 'teal', 'cyan']

garments = ['hat', 'belt', 'bell bottoms', 'cape', 'trench coat']

pairs = [(x, y) for x in range(3) for y in range(2)]

combos = [color + ' ' + garment for color in colors for garment in garments]

brief_combos = [color + ' ' + garment for color in colors for i, garment in enumerate(garments) if i % 2 != 0 or i == 0]

print(brief_combos)


