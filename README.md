# Swiftbar Plugins

This is the set of plugins that I use for [Swiftbar.app](https://swiftbar.app). I don't have many, but I document them all with a little readme inside of every folder.

# Environment Variables
I've found the most reliable way to use envorinment variables within Swiftbar Plugins is to call them each time before the script is run.

I created an example file `env.vars.example` which you can use as a template for your `private/env.vars` file.

## Private Plugins
Some of my plugins check local only services on my network and are not interesting for anyone else. Those are stored within my "private" folder. If you clone this repo, you can use that folder in the exact same way. I'm never going to push anything into that folder. 

A `.sh` file for running these scripts should be something like `private-SCRIPTNAME.10s.sh`