walle_counter = 0
eve_counter = 0
parenthesis = False

script = open("walle.txt", "r")
for line in script:
    for word in line.split():
        if word[0] == '(':
            parenthesis = True
            continue
        if word[-1] == ')':
            parenthesis = False
            continue
        if word[-1] == ':':
            continue
        if "WALL-E" in word and parenthesis == False:
            walle_counter += 1
        if "EVE" in word and parenthesis == False:
            eve_counter += 1
script.close()
print("WALL-E: ", walle_counter)
print("EVE: ", eve_counter)

