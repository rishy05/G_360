import string
import random


def pass_gen():
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase
    
    s3 = string.digits
    
    s4 = string.punctuation
    
    plen = random.randint(12,16)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    

    ps = "".join(random.sample(s, plen))


    return ps

