COLOURS = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aqua": "#00ffff", "ashgrey": "#b2beb5", "barnred": "#7c0a02",
           "bitterlemon": "#cae00d", "black": "#000000", "bole": "#79443b", "bronze": "#cd7f32", "burntsienna": "e97451"}
for colour in COLOURS:
    print(f"{colour}")
choice = input("Colour: ").lower()
while choice != "":
    try:
        print(f"{choice}'s colour code is {COLOURS[choice]}")
    except KeyError:
        print("Colour not in list")
    choice = input("Colour: ").lower()
