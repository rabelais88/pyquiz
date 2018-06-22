# -*- coding: utf-8 -*-
import json
import random
import re
JSONFILE = 'rooms.json'


def pause():
  _tmp = input('...')


def openjson(jsonfile):
  with open(jsonfile) as _f:
    return json.load(_f)


def quiz(_data):
  print('방번호 퀴즈\n그만 둘 때에는 Ctrl+Z를 누르세요.\n...이 나오면 아무키나 누르세요.')
  _annex = input('별관을 맞추시겠어요?(Y/N)')
  _annex = _annex.lower()
  _finishsearch = False
  if _annex != 'y' and _annex != 'n':
    print('잘못된 입력입니다. 별관을 맞추지 않는 것으로 합니다')
    _finishsearch = True
  else if _annex == 'n':
    _finishsearch = True
  
  # loop until it matches the correct room number
  while True:
    _target = random.randint(0, len(_data))
    while not _finishsearch:
      _target = random.randint(0, len(_data))
      if not re.fullmatch(r'(1.*)', _data[_target]['ROOM']):
        _finishsearch = True

    _targetroom = _data[_target]
    _roomno = _data[_target]['ROOM']
    print('방번호 {}의 침대는?'.format(_roomno))
    pause()
    print(_targetroom['BED'])
    print('\n\n\n')
    print('방번호 {}의 타입은?'.format(_roomno))
    pause()
    print(_targetroom['TYPE'])
    print('\n\n\n')
    print('방번호 {}의 뷰는?'.format(_roomno))
    pause()
    print(_targetroom['VIEW'])
    print('\n\n\n')
    print('방번호 {}의 특징은?'.format(_roomno))
    pause()
    print(_targetroom['PS'])
    print('------------------------------------------')
    pause()
    print('\n\n\n')

quiz(openjson(JSONFILE))