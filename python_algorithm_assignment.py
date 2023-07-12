def hours_to_minutes(x):
    result = x*60
    return result
print(hours_to_minutes(3))

def htm_or_mth(x):
    choice = input("hours or minutes")
    if choice == "hours":
        result = x*60
    else:
        result = x/60
    return result
print(htm_or_mth(3))

def wordlen():
    word = input("Enter a word: ")
    letter_count = len(word)
    print(f"The word '{word}' contains {letter_count} letters.")

wordlen()
