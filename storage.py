#python3

'''Storage Class that writes and read query data to local file'''
class Storage():
    def __init__(self):
        d = eval(open('db.txt', 'r').read())
        if not d:
            d = {}
        self.data = d

    def write(self, resp):
        self.data[resp] = True
        target = open('db.txt', 'w')
        target.write(str(self.data))

    def read(self):
        d = open('db.txt', 'r').read()
        return eval(d)
