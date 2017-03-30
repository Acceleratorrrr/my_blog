import re


class Regex(object):
    def __init__(self, test):
        if re.match(r'^\d{3}-\d{3,8}$', test):
            print 'OK'
        else:
            print 'failed'


regex = Regex('010-12345')

re.match(r'^\d{3}-\d{3,8}$', '010-12345')