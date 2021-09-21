if application "Spotify" is running then
	tell application "Spotify"
		if player state is playing then
			set trackText to my trackInfo()
			set artistText to my artistInfo()
			set albumText to my albumInfo()
			return trackText & " - " & artistText & " | symbolize=true\n---\nAlbum: " & albumText
		else
			return ":pause: | symbolize=true\n---\nNothing playing on Spotify"
		end if
	end tell
else
	return ":music.note: | symbolize=true\n---\nSpotify not running"
end if
on trackInfo()
	try
		tell application "Spotify"
			return name of current track
		end tell
	on error
		return "Oops. Couldn't get track info"
	end try
end trackInfo
on artistInfo()
	tell application "Spotify"
		return artist of current track
	end tell
end artistInfo
on albumInfo()
	tell application "Spotify"
		return album of current track
	end tell
end albumInfo
