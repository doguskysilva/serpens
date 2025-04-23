import collections
import re
import sys

WORD_RE = re.compile(r"\w+")

index = collections.defaultdict(list)


def read_text():
    with open(sys.argv[1], encoding="utf-8") as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
