#!/usr/bin/env python
if __package__ == 'iac':
    import iac.parser as parser
else:
    import parser
import atexit
import os
import readline
import rlcompleter

historyPath = os.path.expanduser("~/.pyhistory")


def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath


def main():
    while True:
        try:
            user_input = input('iaci> ')
        except EOFError:
            break
        if user_input:
            result = parser.parse(user_input)
            print(".....", result)


if __name__ == "__main__":
    main()
