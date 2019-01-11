# -*- coding: utf-8 -*-
# vim:set expandtab tabstop=4 shiftwidth=4:
#
# The MIT License (MIT)
# Copyright (c) 2014 Carpentier Pierre-Francois

# Generic imports
import sys
import re
import traceback
import logging
import logging.handlers


def get_loglevel(level):
    """ return logging level object
    corresponding to a given level passed as
    a string
    @str level: name of a syslog log level
    @rtype: logging, logging level from logging module
    """
    if level == 'debug':
        return logging.DEBUG
    elif level == 'notice':
        return logging.INFO
    elif level == 'info':
        return logging.INFO
    elif level == 'warning' or level == 'warn':
        return logging.WARNING
    elif level == 'error' or level == 'err':
        return logging.ERROR
    elif level == 'critical' or level == 'crit':
        return logging.CRITICAL
    elif level == 'alert':
        return logging.CRITICAL
    elif level == 'emergency' or level == 'emerg':
        return logging.CRITICAL
    else:
        return logging.INFO


def get_logger(log_level, log_types, label):
    logger = logging.getLogger(label)
    logger.setLevel(log_level)
    for i in log_types:
        if i == 'null':
            handler = logging.handlers.NullHandler()
        if i == 'syslog':
            handler = logging.handlers.SysLogHandler('/dev/log')
        elif i == 'stderr':
            handler = logging.StreamHandler(sys.stderr)
        elif i == 'stdout':
            handler = logging.StreamHandler(sys.stdout)
        elif i == 'file':
            handler = logging.FileHandler(log_types[i]['file'])
        handler.setLevel(log_level)
        logger.addHandler(handler)
    return logger


def get_loggers(config, debug):
    loggers = {}
    # configure the logger (log level, log type, etc)
    for t in ['app', 'access', 'error']:
        logger_key = t + '_logger'
        logfile_key = t + '_logfile'
        loglevel_key = t + '_loglevel'
        if debug:
            loglvl = get_loglevel('debug')
        elif t == 'error':
            loglvl = get_loglevel('error')
        else:
            loglvl = get_loglevel(config['log'][loglevel_key])

        
        _log_types =  re.split(r', *', config['log'][logger_key])
        if debug and 'stderr' not in _log_types:
            _log_types.append('stderr')

        log_types = {}
        for l in _log_types:
            log_types[l] = None
            if l == 'file':
                log_types[l] = {'file': config['log'][logfile_key]}

        logger = get_logger(loglvl, log_types, 'certascale-' + t)
        loggers[t] = logger
    return loggers
