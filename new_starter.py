import random

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
