[![Build Status](https://travis-ci.org/salc1-org/salbot.svg?branch=master)](https://travis-ci.org/salc1-org/salbot)

Info
------
This is a custom, one use discord bot, nothing cool.

**Commands**
------
* !ping -- gets a latency of the bot
* !restart -- restarts and checks for updates
* !addMember -- adds a member to the member role
* !removeMember -- removes a member from the member role
* !info|userinfo|ui -- gets the current status of a user (nickname, game, voice channel, join discord date, join server date)

**Todo**
------
- [x] Make commands allowed to specific roles.
- [x] Automate the new member role process
- [x] Figure out embeding
- [x] Add/Remove role command for new members.
- [x] Add Cooldowns to commands
- [x] Profile Information Command
- [x] Auto update from git commits
- [ ] Make channels in faq use category IDs not channel IDs


**Long term Todo**
------
Automaticaly delete:
- [x] Messages (to prevent spam)
- [x] Invite Links
- [x] Words that start with N

# How to run

Clone the git repository with `git clone https://github.com/salc1-org/salbot`
Next, change to the salbot directory with `cd salbot`
You'll need to create a file named `.env` under `./salbot-secrets`, and in the .env file:
```
TOKEN=YourTokenHere
BOT_LOG_CHANNEL=
BOT_ERRORS_CHANNEL=
BOT_AUTOMATION_CHANNEL=
MEMBER_RANKUP_CHANNEL=
```
where each of the fields are set to the correct value, note that it is possible to use the same channel ID for each.

# Functions of the cogs

### automaticus_yeetus.py
automatically kicks users from a voice channel they're in if they stay deafened for more than 30 seconds

### backup.py
unimplemented - backs up the server to a backup server

### badwords.py
automatically removes words by regex from the server

### faq.py
deprecated - responds to user messages for common questions

### faqv2.py
responds to user messages for common questions - now uses a json file for the faq responses

### general.py
adds ping and restart commands

### logging.py
implements logging to the salbot log channels

### member_management.py
allows for PCA and above to use !addmember and !removemember to add and remove members

### serverstatus.py
lets you use !server to see the status of 2b2t.org

### tosbot.py
adds !tos and !dgl commands from tos.json / dgl.json

### user_info.py
shows user info such as account creation date, server join date, voice channels, user id, etc.

### pingpunisher.py
Punishes a user in multiple channels by pinging them if they ping *all* mods! Reverse card!