import json
import os
from app.rabbit_subscriber.channel import create_channel




def topic_consume(queue: str, exchange: str, routing_key: str, callback):
    with create_channel() as channel:
        channel.queue_declare(
            queue=queue,
            durable=True
        )
        channel.queue_bind(
            exchange=exchange,
            queue=queue,
            routing_key=routing_key
        )

        channel.basic_consume(queue=queue, on_message_callback=callback)
        channel.start_consuming()

