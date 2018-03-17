#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from src.interface import Interface
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DispatcherHandlerStop


if __name__ == '__main__':

    with open('token', mode='r') as f:
        __token__ = f.readline()

    with open('users', mode='r') as f:
        users = f.readlines()
        users = map(lambda s: int(s), users)

    updater = Updater(__token__)
    dispatcher = updater.dispatcher

    interface = Interface(users)

    start_handler = CommandHandler('start', interface.start)
    check_handler = CommandHandler('squeue_me', interface.check_queue)
    checkall_handler = CommandHandler('squeue_all', interface.check_queue)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(check_handler)
    dispatcher.add_handler(checkall_handler)

    updater.start_polling()
    updater.idle()
