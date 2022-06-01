import re

closers = ['.','?','!','...']

def count_chars(s,chars):
    return sum([s.count(c) for c in chars])

def sent_good(sent):
    if  sent[-1] in closers and count_chars(sent,closers)>1 and not sent.count('"')%2 and not len(re.findall('\(|\)', sent))%2:
        return True
    elif sent[-1] in closers and len(sent)>40:
        return True
    else:
        return False
