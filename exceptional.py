'''exceptions handling'''
import sys
from math import log

def convert(s):
  try:
    return int(s)
  except (ValueError, TypeError) as ex:
    print("error : {}".format(str(ex)),file=sys.stderr),
    raise

def string_log(s):
  return log(convert(s))