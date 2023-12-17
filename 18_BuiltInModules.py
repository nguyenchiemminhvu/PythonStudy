import os
import sys
import urllib.request
import zlib
import timeit

os.system("git status")
sys.stdout.write("write text to stdout file stream\n")
sys.stderr.write("write text to stderr file stream\n")

s = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(s, len(s))
s = zlib.compress(s)
print(s, len(s))
s = zlib.decompress(s)
print(s, len(s))

request = """
import urllib.request
with urllib.request.urlopen("https://www.google.com") as response:
    for line in response:
        print(line)
"""
time_cost = timeit.timeit(request, number=1)
print(time_cost, "seconds")