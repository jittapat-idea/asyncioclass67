# https://aiokafka.readthedocs.io/en/stable/
from aiokafka import AIOKafkaConsumer 
from aiokafka.admin import AIOKafkaAdminClient , NewTopic
import asyncio

async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic', 'my_other_topic',
        bootstrap_servers='192.168.137.25:9094',#localhost
        group_id="my-group")
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()



asyncio.run(consume())