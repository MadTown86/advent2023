import re

"""
I need to learn this for strings
"""

stringexample1 = "ThisThisThatThisThat"
stringexample2 = "one1Twonethreeighteenine2"

def main(inp: str) -> list:
    res = []
    for i in re.search(r'This', inp):
        res.append(i.group(1))
    return res

print(main(stringexample1))