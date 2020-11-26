# Discord-Breakout-Rooms
A discord bot that organises users in a voice chat into breakout rooms, not unlike zoom or blackboard collaborate.


## Usage
`/breakout <number of rooms you want>`

The bot will then randomly and evenly distribute the users into different voice chats. The default number of rooms is 3.

## Setup

The only dependency needed is discord.py which can be installed from [here](https://discordpy.readthedocs.io/en/latest/intro.html). 

Currently the bot will only work if it has the `Administrator` permission checked in its role settings, i'm looking into finding a  workaround for this but for now, since the bot doesnt touch anything sensitve, it will be okay.

No other special permissions are needed. Rename config-template.py to config.py and add the relevant information and you're good to go.

If there are any bugs or if you have any suggests you are free to make a PR or annoy me.
