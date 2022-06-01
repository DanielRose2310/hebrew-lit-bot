import re
closers = ['.','?','!']
def sent_good(sent):
    if  sent[-1] in closers and len(sent>10) and not sent.count('"')%2 and not len(re.findall('\(|\)', sent))%2:
        return True
    else:
        return False
