#!/usr/bin/env python
# coding=utf-8
import pika

from settings import URI
params = pika.URLParameters(URI)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology! sys-29-sdb-04')
connection.close()