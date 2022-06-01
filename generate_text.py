import random
from string import punctuation
import re 
from validate_sent import sent_good

def generate_text(model, state_size=2, min_length=20):
    '''
    Consume a Markov chain model (make sure to specify the <state_size> used)
    to generate text that is at least <min_length> size long.
    '''
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
            next_word = random.choice(model[key])
        text.append(next_word)
        i += 1
        if i > min_length and text[-1][-1] == '.' and sent_good(' '.join(text)):
            break
    return ' '.join(text)
