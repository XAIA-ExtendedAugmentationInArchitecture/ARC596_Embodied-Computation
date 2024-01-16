import time

from compas_eve import Message
from compas_eve import Publisher
from compas_eve import Subscriber
from compas_eve import Topic

host = Host()
topic = Topic("/compas_eve/hello_robot/", Message)

publisher = Publisher(topic)
subcriber = Subscriber(topic, callback=lambda msg: print(f"Received message: {msg.text}"))
subcriber.subscribe()

for i in range(20):
    msg = Message(text=f"Hello robot #{i}")
    print(f"Publishing message: {msg.text}")
    publisher.publish(msg)
    time.sleep(1)
