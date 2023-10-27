# Karuha

[![License](https://img.shields.io/github/license/Ovizro/Karuha.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/KaruhaBot.svg)](https://pypi.python.org/pypi/KaruhaBot)
![Python Version](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11-blue.svg)

A simple Tinode chatbot framework.

The name of the library `Karuha` comes from the character Karuha Ramukone (カルハ・ラムコネ) in the game 星空鉄道とシロの旅.

<center>

![Karuha](https://raw.githubusercontent.com/Visecy/Karuha/master/docs/img/tw_icon-karuha2.png)

</center>

> カルハ・ラムコネと申します。カルハちゃんって呼んでいいわよ

## Installation

From pip:

    pip install KaruhaBot

From source code:

    python setup.py install

## Quick Start

Create a new file `config.json` and write the following content:

```json
{
    "server": {
        "host": "localhost:16060",
        "listen": "0.0.0.0:40051"
    },
    "bots": [
        {
            "name": "chatbot",
            "schema": "basic",
            "secret": "{chatbot_login_name}:{chatebot_login_passwd}"
        }
    ]
}
```

> Replace `{chatbot_login_name}` and `{chatebot_login_passwd}` with the chatbot’s login account name and password in the Tinode server.

Start the chatbot using the following command:

    python -m Karuha ./config.json

You can now see the messages others have sent to the chatbot from the command line.Yeah, that's it, no more. 

## Go Further?

Well, you can actually go a step further and send messages to users.

Currently, if you want to reply to a message, you currently need to add a handler for the event yourself. This is not a simple process. Fortunately, we are about to introduce a command module to improve this.

Because this is a relatively low-level function, I will only give an example to show how karuha is currently used in python:

```python
import karuha
from karuha import Bot, DataEvent


bot = Bot(
    "basic",
    "chatbot:123456"
)


@karuha.on(DataEvent)
async def reply(event: DataEvent) -> None:
    if event.server_message.content.decode() == "\"Hello chatbot!\"":    # message.content is a json string
        await event.bot.publish(
            event.server_message.topic,
            "Hello world!"
        )


if __name__ = "__main__":
    karuha.load_config()
    karuha.add_bot(bot)
    karuha.run()
```


