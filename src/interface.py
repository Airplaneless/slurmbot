#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import datetime
import os


def usr2str(usr):
    return "{} {} ({})".format(
        usr['first_name'],
        usr['last_name'],
        usr['username']
    )


class Interface:

    def __init__(self):
        time = datetime.datetime.now()
        log_file = os.path.abspath('bot_logs/bot_{0}_{1}_{2}.log'.format(time.year, time.month, time.day))
        if not os.path.exists(os.path.abspath('bot_logs/')):
            os.mkdir(os.path.abspath('bot_logs/'))
        if not os.path.exists(log_file):
            os.mknod(log_file)

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s %(message)s'
        )

    @staticmethod
    def start(bot, update, args):
        user = update.message.from_user
        for arg in args:
            print arg
        logging.info('Hi to {}'.format(usr2str(user)))
        bot.send_message(chat_id=update.message.chat_id, text=u"Hello there")

    @staticmethod
    def check_queue(bot, update):
        user = update.message.from_user
        logging.info('check queue for {}'.format(usr2str(user)))
        os.system('squeue -u u0052 > workspace/queue.txt')
        with open('queue.txt', mode='r') as f:
            text = f.readlines()
        bot.send_message(chat_id=update.message.chat_id, text='\n'.join(text))

    @staticmethod
    def check_queue_all(bot, update):
        user = update.message.from_user
        logging.info('check all queue for {}'.format(usr2str(user)))
        os.system('squeue > workspace/queue_all.txt')
        with open('queue.txt', mode='r') as f:
            text = f.readlines()
        bot.send_message(chat_id=update.message.chat_id, text='\n'.join(text))