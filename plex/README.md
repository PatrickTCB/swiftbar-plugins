# Plex Status
This gives you the playback status from a given Plex server for a specific user.

Currently it's written to support Audio Books, Music, TV, & Movies because that's what's in my own Plex library. 

Depending on your setup you may want to adapt the `isMyPC` function so that it can determine if a given device is yours. The idea here is that device information gets added when you're on a device other than your Mac, but it gets ommitted when you're on your Mac. 