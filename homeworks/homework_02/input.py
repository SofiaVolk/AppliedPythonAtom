import sys
import csv
import json
import tempfile


def encode(object):
    encoding = [
        'utf-8',
        'utf-16',
        'cp-1251'
    ]
    for enc in encoding:
        try:
            open(object, encoding=enc).read()
        except (UnicodeDecodeError, LookupError, UnicodeError):
            pass
        else:
            return enc
    return 0


def code(data, enc):
    with open(data, 'r', encoding=enc) as f:
        try:
            reader = json.load(f)
            f.seek(0)
        except Exception:
            pass
        else:
            return reader


def parser(object):
    enc = encode(object)
    if code(object, enc):
        with open(object, 'r', encoding=enc) as f:
            try:
                reader = json.load(f)
                for line in f:
                    reader.append(line)
                f.seek(0)
                return reader
            except Exception:
                return r'Формат не валиден'
    else:
        with open(object, 'rt', encoding=enc) as f:

            reader1 = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for line in f:
                reader.append(line)
            f.seek(0)
            reader = list(reader1)
            return reader
