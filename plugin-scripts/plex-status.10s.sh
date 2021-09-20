#!/bin/bash

# <bitbar.title>Plex Status - Improved</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Patrick Coffey</bitbar.author>
# <bitbar.author.github>patricktcb</bitbar.author.github>
# <bitbar.desc>See what's currently playing on your Plex Server</bitbar.desc>
# <bitbar.image>https://res.cloudinary.com/cyberge/image/upload/v1550627901/icons/plex_878759_eey690.png</bitbar.image>
# <bitbar.dependencies>python, bash</bitbar.dependencies>
# <swiftbar.hideSwiftBar>true</swiftbar.hideSwiftBar>
# <swiftbar.hideDisablePlugin>true</swiftbar.hideDisablePlugin>
# <swiftbar.hideAbout>true</swiftbar.hideAbout>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>
PLEX_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SCRIPT_DIR="$(dirname "$PLEX_SCRIPT_DIR")"
source $SCRIPT_DIR/private/env.vars
python3 $SCRIPT_DIR/plex/main.py