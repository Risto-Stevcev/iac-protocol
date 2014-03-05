#!/usr/bin/env python
import socket
import select
import threading
import sys
import argparse
import iac.parser as parser

__package__ = "IAC Protocol"
__author__ = "Risto Stevcev"
__version__ = "0.1"


def enum(**enums):
    return type('Enum', (), enums)
Protocol = enum(UDP=socket.SOCK_DGRAM, TCP=socket.SOCK_STREAM)


class Message(object):
    client_started = "[+] Client connected"
    client_sent = "[+] Client sent"

    timeout = "[!] Clients timed out."
    keyboard_interrupted = "[!] Keyboard interrupted."
    socket_error = "[!] Socket error"
    exit_wait = "[!] Exiting... Waiting on clients."
    exit = "[!] Done."


class Client(threading.Thread):
    def __init__(self, socket, buffer_size, log_file=sys.stdout):
        threading.Thread.__init__(self)
        self.client, self.address = socket
        self.buffer_size = buffer_size
        self.log_file = log_file

        ip, port = self.address
        self.log_file.write("%s: [%s:%d]\n" % (Message.client_started, ip, port))

    def run(self):
        while True:
            data = self.client.recv(self.buffer_size)
            result = parser.parse(data.decode())

            if data:
                if result is True or result is False:
                    result = str(result) 
                self.client.send(result.encode())
            else:
                self.client.close()
                break


class Server(object):
    LOCALHOST = ''
    PORT = 14733
    BACKLOG = 5
    BUFFER_SIZE = 1024
 
    def __init__(self, port=PORT, protocol=Protocol.UDP, timeout=None, backlog=BACKLOG, 
            buffer_size=BUFFER_SIZE, log_file=sys.stdout):
        self.socket = None
        self.clients = []

        self.host = Server.LOCALHOST
        self.port = port
        self.protocol = protocol

        self.timeout = timeout
        self.backlog = backlog 
        self.buffer_size = buffer_size
        self.log_file = log_file

    def listen(self):
        try:
            self.socket = socket.socket(socket.AF_INET, self.protocol)
            self.socket.bind((self.host, self.port))
            if self.protocol == Protocol.TCP:
                self.socket.listen(self.backlog)

        except socket.error as e:
            if self.socket:
                self.socket.close()
            self.log_file.write("%s: %s\n" % (Message.socket_error, str(e)))
            sys.exit(1)

    def run(self):
        self.listen()
        input = [self.socket, sys.stdin]

        listening = True
        while listening:
            try:
                ready_to_read, ready_to_write, in_error = select.select(input, [], [], self.timeout)
            except KeyboardInterrupt:
                self.log_file.write("%s\n" % Message.keyboard_interrupted)
                break

            if len(ready_to_read) == 0:
                self.log_file.write("%s\n" % Message.timeout)
                break

            if self.protocol == Protocol.TCP:
                listening = self.read_TCP(ready_to_read, listening)
            elif self.protocol == Protocol.UDP:
                listening = self.read_UDP(ready_to_read, listening)

        if self.protocol == Protocol.TCP:
            self.close_all_sockets()
        elif self.protocol == Protocol.UDP:
            self.log_file.write("%s\n" % Message.exit)

    def read_TCP(self, ready_to_read, listening):
        for client in ready_to_read:
            if client == self.socket:
                client_socket = Client(self.socket.accept(), self.buffer_size, self.log_file)
                client_socket.start()
                self.clients.append(client_socket)

            elif client == sys.stdin:
                data = sys.stdin.readline()
                if data == "":
                    listening = False
        return listening

    def read_UDP(self, ready_to_read, listening):
        for client in ready_to_read:
            if client == self.socket:
                message, client_address = self.socket.recvfrom(self.buffer_size)
                ip, port = client_address
                self.log_file.write("%s [%s:%d]: %s\n" % (Message.client_sent, ip, port, message))

                result = parser.parse(message.decode())
                if result is True or result is False:
                    result = str(result)
                self.socket.sendto(result.encode(), client_address)

            elif client == sys.stdin:
                data = sys.stdin.readline()
                if data == "":
                    listening = False
        return listening
 
    def close_all_sockets(self):
        self.log_file.write("%s\n" % Message.exit_wait)

        self.socket.close()
        for client in self.clients:
            client.join()

        self.log_file.write("%s\n" % Message.exit)

# Parse command line arguments
argparser = argparse.ArgumentParser(description='Server for %s %s - by %s.' % (__package__, __version__, __author__))
argparser.add_argument('-p', '--port', type=int, nargs=1, default=Server.PORT, 
        help='server port (default: %d)' % Server.PORT)
argparser.add_argument('-s', '--buffer-size', type=int, nargs=1, default=Server.BUFFER_SIZE, 
        help='buffer size (default: %d)' % Server.BUFFER_SIZE)
argparser.add_argument('-t', '--timeout', type=int, nargs=1, default=None, 
        help='server timeout (default: None)')
argparser.add_argument('-b', '--backlog', type=int, nargs=1, default=Server.BACKLOG, 
        help='maximum connections (default: %d)' % Server.BACKLOG)
argparser.add_argument('-l', '--log-file', type=argparse.FileType('w'), default=sys.stdout, 
        help='log file (default: stdout)')

group = argparser.add_mutually_exclusive_group()
group.add_argument('--tcp', action='store_const', const=Protocol.TCP, dest='protocol', 
        help='TCP connection')
group.add_argument('--udp', action='store_const', const=Protocol.UDP, dest='protocol', 
        help='UDP connection (default)')
argparser.set_defaults(protocol=Protocol.UDP)
args = argparser.parse_args()

def main():
    if type(args.port) is list:
        port = args.port[0]
    else:
        port = args.port
    s = Server(port=port, timeout=args.timeout, backlog=args.backlog, log_file=args.log_file, 
            buffer_size=args.buffer_size, protocol=args.protocol)
    s.run() 

if __name__ == "__main__":
    main()
