#!/usr/bin/env python
# coding=utf-8
import pika

from settings import URI
params = pika.URLParameters(URI)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True,
    consumer_tag='Netology sys-29-sdb-04')
channel.start_consuming()