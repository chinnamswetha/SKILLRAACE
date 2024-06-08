subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket","Ludo"]
for sub in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = sub + " " + verb + " " + obj + "."
            print(sentence)