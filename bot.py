#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
from src.interface import Interface
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, DispatcherHandlerStop


if __name__ == '__main__':

    with open('config.json', mode='r') as f:
        config = json.load(f)

    updater = Updater(config['token'])
    dispatcher = updater.dispatcher

    interface = Interface(config['allowed_users'], config['output_dir'])

    start_handler = CommandHandler('start', interface.start)
    check_handler = CommandHandler('squeue_me', interface.check_queue)
    checkall_handler = CommandHandler('squeue_all', interface.check_queue_all)
    check_space_handler = CommandHandler('diskspace', interface.check_disk_space)
    check_progress_handler = CommandHandler('progress', interface.check_progress)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(check_handler)
    dispatcher.add_handler(checkall_handler)
    dispatcher.add_handler(check_space_handler)
    dispatcher.add_handler(check_progress_handler)

    updater.start_polling()
    updater.idle()
