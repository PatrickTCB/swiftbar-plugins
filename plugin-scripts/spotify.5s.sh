#!/bin/bash

# <bitbar.title>Spotify Status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Patrick Coffey</bitbar.author>
# <bitbar.author.github>patricktcb</bitbar.author.github>
# <bitbar.desc>See what's currently playing on Spotify</bitbar.desc>
# <bitbar.dependencies>applescript, bash</bitbar.dependencies>
# <swiftbar.hideSwiftBar>true</swiftbar.hideSwiftBar>
# <swiftbar.hideDisablePlugin>true</swiftbar.hideDisablePlugin>
# <swiftbar.hideAbout>true</swiftbar.hideAbout>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>
PLEX_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SCRIPT_DIR="$(dirname "$PLEX_SCRIPT_DIR")"
osascript $SCRIPT_DIR/spotify/main.scpt