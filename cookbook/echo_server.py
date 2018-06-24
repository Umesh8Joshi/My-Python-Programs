'''
A file that will create a echo server
author: Umesh8Joshi
alias: youm3sh
'''

from socketserver import StreamRequestHandler, TCPServer
from functools import partial

class EchoHandler(StreamRequestHandler):
    # a simple echo server
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handler(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

def main():
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECIVED!!'))
    serv.serve_forever()

if __name__ == "__main__":
    main()
