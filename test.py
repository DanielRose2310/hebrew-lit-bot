from validate_sent import sent_good

def get_new_starter(model):
    model_size = len([s.split(' ') for s in model.keys()])
    
    def get_start_value():
        rand_val = random.randint(0,model_size)
        starter = list(model.keys())[rand_val]
        pre_starter = list(model.keys())[rand_val-1]
        gen_start=[pre_starter,starter]
        return gen_start
    
    start_value = ['123','123']
    while True :
        start_value = get_start_value()
        if '.'  in start_value[0][0:-2] or '!'  in start_value[0][0:-2] or '.'  in start_value[0][0:-2]:
            break
    good_start = start_value[1].split(' ')
    return good_start

def generate_text(model, state_size=2):
    
    text = get_new_starter(model)
    i = state_size
    while True:
        key = ' '.join(text[i-state_size:i])
        if key not in model:
            text += get_new_starter(model)
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
