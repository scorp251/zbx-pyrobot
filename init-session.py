# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import sys
from app.utils import log
from pyrogram import Client

"""This example demonstrates a basic API usage"""

# Create a new Client instance
tgclient = Client("telegram", config_file='conf/config.ini')

# Start the Client before calling any API method
tgclient.start()

# Send a message to yourself, Markdown is enabled by default
tgclient.send_message("me", "Hi there! I'm using **Pyrogram**")

# Send a location to yourself
tgclient.send_location("me", 51.500729, -0.124583)

# Stop the client when you're done
tgclient.stop()
