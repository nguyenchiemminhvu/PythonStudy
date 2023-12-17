import os
import sys
import logging
import urllib.request
import zlib
import timeit
import textwrap
import array

os.system("git status")
sys.stdout.write("write text to stdout file stream\n")
sys.stderr.write("write text to stderr file stream\n")


logging.basicConfig(level=logging.INFO)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

s = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(s, len(s))
s = zlib.compress(s)
print(s, len(s))
s = zlib.decompress(s)
print(s, len(s))
print(textwrap.fill(str(s), width=10))

request = """
import urllib.request
with urllib.request.urlopen("https://www.google.com") as response:
    for line in response:
        print(line)
"""
time_cost = timeit.timeit(request, number=1)
print(time_cost, "seconds")