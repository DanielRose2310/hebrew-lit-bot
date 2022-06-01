import random
from string import punctuation
import re 
from validate_sent import sent_good

def generate_text(model, state_size=2):

    def get_new_starter():
        return random.choice([s.split(' ') for s in model.keys() if not any(p in s for p in punctuation)])
    text = get_new_starter()

    i = state_size
    while True:
        key = ' '.join(text[i-state_size:i])
        if key not in model:
            text += get_new_starter()
            i += 1
            continue

        next_word = random.choice(model[key])
        if ')' in next_word and not '(' in ' '.join(text):
            get_new_starter()
        text.append(next_word)
        i += 1
        if sent_good(' '.join(text)):
            break
    return ' '.join(text)
