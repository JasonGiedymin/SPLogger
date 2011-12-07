from time import strftime
import math
import abc

'''
Simple Python Logger
'''

LOGGING_LEVEL_DEBUG = 'DEBUG'
LOGGING_LEVEL_INFO = 'INFO'
LOGGING_LEVEL_WARN = 'WARN'
LOGGING_LEVEL_ERROR = 'ERROR'
LOGGING_LEVEL_FATAL = 'FATAL'
LOGGING_LEVELS = [  LOGGING_LEVEL_DEBUG,
                    LOGGING_LEVEL_INFO,
                    LOGGING_LEVEL_WARN,
                    LOGGING_LEVEL_ERROR,
                    LOGGING_LEVEL_FATAL ]
LOGGING_LEVEL = LOGGING_LEVEL_INFO


LOGGER_OUTPUT_TYPE_STDOUT = 'STD'
LOGGER_OUTPUT_TYPE_MEM = 'MEM'
LOGGER_OUTPUT_TYPE_NOSQL = 'NOSQL'
LOGGER_OUTPUT_TYPES = [ LOGGER_OUTPUT_TYPE_STDOUT,
                        LOGGER_OUTPUT_TYPE_MEM,
                        LOGGER_OUTPUT_TYPE_NOSQL ]
LOGGER_OUTPUT_TYPE = LOGGER_OUTPUT_TYPE_STDOUT

# -------------------------------------------------------------------

class AbstractLoggerOutput(object):
  ''' Abstract Logger Ouput '''

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def record(cls, msg_type, sub_key, msg, pre, post):
    pass


class StdLoggerOutput(AbstractLoggerOutput):
  ''' Std Output '''

  _timestamp_format = '%a, %d %b %Y %H:%M:%S %z'
  _master_key = 'splogger_master'

  @classmethod
  def record(cls, msg_type, sub_key, msg, pre, post):
    print "%s %s - [%s]: %s%s" % (pre, msg_type, strftime(cls._timestamp_format), msg, post)


class MemLoggerOutput(AbstractLoggerOutput):
  ''' Memory Output '''

  @classmethod
  def record(cls, msg_type, sub_key, msg, pre, post):
    raise Exception, "Logging type not implemented yet!"

class NoSQLLoggerOutput(AbstractLoggerOutput):
  ''' NoSQL Output '''

  @classmethod
  def record(cls, msg_type, sub_key, msg, pre, post):
    raise Exception, "Logging type not implemented yet!"


LOGGER_FACTORY = {  LOGGER_OUTPUT_TYPE_STDOUT: StdLoggerOutput,
                    LOGGER_OUTPUT_TYPE_MEM: MemLoggerOutput,
                    LOGGER_OUTPUT_TYPE_NOSQL: NoSQLLoggerOutput }


class AbstractLogger(object):
  ''' Abstract Logger '''

  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def _logit(cls, msg_type, sub_key, msg, pre, post):
    pass

  @abc.abstractmethod
  def info(cls, msg, sub_key="", pre="", post=""):
    ''' Direct info logger '''
    pass
  
  @abc.abstractmethod
  def debug(cls, msg, sub_key="", pre="", post=""):
    ''' Direct debug logger '''
    pass
  
  @abc.abstractmethod
  def warn(cls, msg, sub_key="", pre="", post=""):
    ''' Direct warn logger '''
    pass

  @abc.abstractmethod
  def error(cls, msg, sub_key="", pre="", post=""):
    ''' Direct error logger '''
    pass
  
  @abc.abstractmethod
  def fatal(cls, msg, sub_key="", pre="", post=""):
    ''' Direct fatal logger '''
    pass


class Logger(AbstractLogger):
  ''' Base Logger Class '''

  @classmethod
  def _logit(cls, msg_type, sub_key, msg, pre, post):
    if LOGGING_LEVELS.index(LOGGING_LEVEL) <= LOGGING_LEVELS.index(msg_type):
      LOGGER_FACTORY[LOGGER_OUTPUT_TYPE]().record(msg_type, sub_key, msg, pre, post)
      #print "%s %s - [%s]: %s%s" % (pre, msg_type, strftime(cls._timestamp_format), msg, post)

  @classmethod
  def debug(cls, msg, sub_key="", pre="", post=""):
    ''' Direct debug logger '''
    cls._logit(LOGGING_LEVEL_DEBUG, sub_key, msg, pre, post)

  @classmethod
  def info(cls, msg, sub_key="", pre="", post=""):
    ''' Direct info logger '''
    cls._logit(LOGGING_LEVEL_INFO, sub_key, msg, pre, post)

  @classmethod
  def warn(cls, msg, sub_key="", pre="", post=""):
    ''' Direct warn logger '''
    cls._logit(LOGGING_LEVEL_WARN, sub_key, msg, pre, post)

  @classmethod
  def error(cls, msg, sub_key="", pre="", post=""):
    ''' Direct error logger '''
    cls._logit(LOGGING_LEVEL_ERROR, sub_key, msg, pre, post)

  @classmethod
  def fatal(cls, msg, sub_key="", pre="", post=""):
    ''' Direct fatal logger '''
    cls._logit(LOGGING_LEVEL_FATAL, sub_key, msg, pre, post)

# -------------------------------------------------------------------

# Should already be setup for level = 'INFO'
# Logger.debug("Hi")
# Logger.info("Hi")
# Logger.warn("Hi")
# Logger.error("Hi")
# Logger.fatal("Hi")





















