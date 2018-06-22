# -*- coding: utf-8 -*-
import json
import csv

CSVFILE = 'data.csv'
JSONFILE = 'rooms.json'


def readcsv(csvfile):
  _res = []
  with open(CSVFILE, 'r') as _csvfile:
    _csvreader = csv.reader(_csvfile)
    _csvrows = []

    for _row in _csvreader:
      _csvrows.append(_row)

    _columns = _csvrows[0]
    _csvrows = _csvrows[1:]

    for _row in _csvrows:
      _tempdict = {}
      for idx, column in enumerate(_columns):
        _tempdict[column] = _row[idx]
      _res.append(_tempdict)
  return _res


def savejson(jsonfile, _data):
  with open(JSONFILE, 'w') as _f:
    json.dump(_data, _f, ensure_ascii=False)


savejson(JSONFILE, readcsv(CSVFILE))