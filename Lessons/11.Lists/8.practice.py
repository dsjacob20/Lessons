
print()

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []

for ew in words:
    if ew[-1] == "e":
        a = "d"
    else:
        a = "ed"
    past_tense.append(ew + a)

print(words)
print(past_tense)

print()