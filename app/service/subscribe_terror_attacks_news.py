from pika.adapters.blocking_connection import BlockingChannel
import json

from toolz import pipe

from app.rabbit_subscriber.subscriber import topic_consume
import os
from app.service.insert_terror_attacks_to_psql_service import insert_data_to_psql_and_elastic
import app.utils.subscriber_utils as convert_utils


EXCHANGE = os.getenv('TERROR_ATTACK_EXCHANGE')
QUEUE = os.getenv('TERROR_ATTACK_QUEUE')
ROUTING_KEY = os.getenv('TERROR_ATTACK_ROUTING_KEY')

def consume_terror_attacks():
    def callback(channel: BlockingChannel, method, props, body):
        terror_attack = pipe(
            body.decode()[7::],
            json.loads,
            convert_utils.terror_attack_dict_to_terror_attack_model
        )
        insert_data_to_psql_and_elastic([terror_attack])
        channel.basic_ack(method.delivery_tag)
        print("message consumed")

    topic_consume(exchange=EXCHANGE,
                   queue=QUEUE,
                  routing_key=ROUTING_KEY,
                  callback=callback)