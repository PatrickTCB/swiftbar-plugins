#!/bin/bash

# <bitbar.title>Network Quality Weather</bitbar.title>
# <bitbar.version>v1.1</bitbar.version>
# <bitbar.author>Patrick Coffey</bitbar.author>
# <bitbar.author.github>patricktcb</bitbar.author.github>
# <bitbar.desc>Displays the network quality</bitbar.desc>
# <bitbar.dependencies>python, bash</bitbar.dependencies>
# <swiftbar.hideRunInTerminal>true</swiftbar.hideRunInTerminal>

PLUGIN_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SCRIPT_DIR="$(dirname "$PLUGIN_SCRIPT_DIR")"
source $SCRIPT_DIR/private/env.vars
/opt/homebrew/bin/python3 $SCRIPT_DIR/network\ quality/main.py