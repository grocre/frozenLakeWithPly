
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL COLUMN FROM SELECT TABLE\n    expression : SELECT term\n    \n    \n    term : factor FROM factor\n    \n    term : factor\n    \n    factor : TABLE\n    \n    factor : COLUMN\n    \n    factor : ALL\n    '
    
_lr_action_items = {'SELECT':([0,],[2,]),'$end':([1,3,4,5,6,7,9,],[0,-1,-3,-4,-5,-6,-2,]),'TABLE':([2,8,],[5,5,]),'COLUMN':([2,8,],[6,6,]),'ALL':([2,8,],[7,7,]),'FROM':([4,5,6,7,],[8,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'term':([2,],[3,]),'factor':([2,8,],[4,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> SELECT term','expression',2,'p_expression','main.py',28),
  ('term -> factor FROM factor','term',3,'p_term','main.py',41),
  ('term -> factor','term',1,'p_term_factor','main.py',47),
  ('factor -> TABLE','factor',1,'p_factor_table','main.py',53),
  ('factor -> COLUMN','factor',1,'p_factor_name','main.py',59),
  ('factor -> ALL','factor',1,'p_factor_all','main.py',65),
]
