def duplicate_count(text):
    setText = set(list(text.lower()))
    return len([a for a in setText if text.lower().count(a) > 1])
   