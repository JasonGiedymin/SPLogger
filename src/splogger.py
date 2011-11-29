from time import strftime
import math

'''
Simple Python Logger
Great for <k,v> stores

Three types of loggers:
- StaticLogger: Access the logger as a static object.
- SingletonLogger: Singleton Class Logger.
- Logger: Class based instantiated logger.

Oh there is a large todo list...
'''

class StaticLogger(object):
  ''' Simple Logger - keep it simple J! '''
  
  _debug = True
  _timestamp_format = '%a, %d %b %Y %H:%M:%S %z'
  _master_key = 'plogger_master'

  @staticmethod
  def _logit(msg_type, sub_key, msg, pre, post):
    print "%s %s - [%s]: %s%s" % (pre, msg_type, strftime(Logger._timestamp_format), msg, post)

  @staticmethod
  def info(msg, pre="", post=""):
    ''' Direct info logger '''
    Logger._logit("INFO", msg, pre, post)
  
  @staticmethod
  def debug(msg, pre="", post=""):
    ''' Direct debug logger '''
    if Logger._debug:
      Logger._logit("DEBUG", msg, pre, post)
  
  @staticmethod
  def error(msg, pre="", post=""):
    ''' Direct error logger '''
    if Logger._debug:
      Logger._logit("ERROR", msg, pre, post)
