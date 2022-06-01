import re
closers = ['.','?','!','...']
def sent_good(sent):
    if  closers in sent[-1] and not sent.count('"')%2 and not len(re.findall('\(|\)', sent))%2:
        return True
    else:
        return False
