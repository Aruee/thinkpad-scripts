#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>
# Licensed under The GNU Public License Version 2 (or later)

'''
Logic for virtual keyboard
'''

import logging
import subprocess

logger = logging.getLogger(__name__)

def toggle(program, state):
    '''
    Toggles the running state of the given progam.

    If state is true, the program will be spawned.

    :param str program: Name of the program
    :param bool state: Desired state
    :returns: None
    '''
    if state:
        command = ['pgrep', program]
        try:
            logger.debug(command)
            subprocess.check_output(command)
        except subprocess.CalledProcessError:
            command = program + '&'
            logger.debug(command)
            subprocess.check_call(command, shell=True)
    else:
        command = ['killall', program]
        logger.debug(' '.join(command))
        subprocess.check_call(command)

