import xml.etree.ElementTree as ET
import urllib.request
import ssl
import os

# plextoken will need to be set manually. You can follow this guide from Plex on how to get one: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
# plexhost should be whatever IP/domain name your local machine uses to connect.
# myuserid is the id of your preferred watcher. This is typically 1, but depending on how your server admin set things up it could be different

def plexMusicInfo(el):
    if el.attrib['librarySectionTitle'] == "Audio Books":
        trackInfo = ":books.vertical.fill: " + el.attrib['parentTitle'] + " by " + el.attrib['grandparentTitle'] + " | symbolize=true\n---\nTrack: " + el.attrib['title']
    else:  
        trackInfo = ":music.note: " + el.attrib['title'] + " by " + el.attrib['grandparentTitle'] + " | symbolize=true\n---\nAlbum: " + el.attrib['parentTitle']
    return trackInfo

def plexMovieInfo(el):
    if el.attrib['librarySectionTitle'] == "Movies":
        trackInfo = ":film.fill: " + el.attrib['title'] + " | symbolize=true"
    else:
        trackInfo = ":video.fill:  " + el.attrib['title'] + " | symbolize=true"
    return trackInfo

def plexTVInfo(el):
    trackInfo = ":tv.fill:  " + el.attrib['grandparentTitle'] + " - " + el.attrib['title'] + " | symbolize=true\n---\n" + el.attrib['parentTitle'] + " Episode " + el.attrib['parentIndex']
    return trackInfo

def plexMediaInfo(mc, myuserid):
    trackInfo = ""
    if mc.find("User").attrib["id"] == myuserid:
        if str(mc.tag) == "Track":
            if mc.find("Player").attrib["state"] == "playing":
                trackInfo = plexMusicInfo(mc)
        elif str(mc.tag) == "Video":
            if mc.find("Player").attrib["state"] == "playing":
                if mc.attrib['type'] == "movie":
                    trackInfo = plexMovieInfo(mc)
                elif mc.attrib['type'] == "episode":
                    trackInfo = plexTVInfo(mc)
        if mc.find("Player").attrib["state"] == "playing":
            trackInfo = trackInfo + "\n---\n" + mc.find("Player").attrib['product'] + " on " + mc.find("Player").attrib['platform']
    return trackInfo

def getPlexStatus(plextoken, plexhost):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # Plex uses self signed certs, so they can't be verified.
    # The context here is setup so that you can use a URL like the one below
    # http://127.0.0.1:32400/status/sessions?X-Plex-Token=myCoolToken
    plexAddress = plexhost + '/status/sessions?X-Plex-Token=' + plextoken 
    plexXML = urllib.request.urlopen(plexAddress, context=ctx).read()
    return plexXML

def isMyPC(mc):
    mypc = False
    if mc.find("Player").attrib['platform'] == "osx" or mc.find("Player").attrib['platform'] == "macOS" or mc.find("remotePublicAddress") == "127.0.0.1":
        mypc = True
    return mypc

def parseXML(rawXML, myuserid):
    tree = ET.ElementTree(ET.fromstring(rawXML))
    root = tree.getroot()
    trackInfo = ""
    onOtherDevices = ""
    if root.attrib['size'] == "1":
        trackInfo = plexMediaInfo(root[0], myuserid)
    else:
        for mc in root:
            if isMyPC(mc):
                trackInfo = plexMediaInfo(mc, myuserid)
            else:
                od = plexMediaInfo(mc, myuserid)
                if od != "":
                    onOtherDevices = onOtherDevices + plexMediaInfo(mc, myuserid) + "\n---\n"
    if trackInfo == "" and onOtherDevices != "":
        trackInfo = onOtherDevices
    elif trackInfo != "" and onOtherDevices != "":
        trackInfo = trackInfo + "\n---\n" + onOtherDevices
    elif trackInfo == "" and onOtherDevices == "":
        trackInfo = "❯\n---\nNothing Playing"
    return trackInfo

#This is the function to be used with the script is called by itself
if __name__ == '__main__':
    plextoken = os.environ['SWIFTBAR_PLEXTOKEN']
    # Plexhost should be something like 'http://127.0.0.1:32400' or 'https://plex.example.com'
    plexhost = os.environ['SWIFTBAR_PLEXHOST']
    myuserid = "1"
    try:
        plexXML = getPlexStatus(plextoken, plexhost)
        print(parseXML(plexXML, myuserid))
    except Exception as e:
        print("🚫\n---\nCould not connect to Plex server " + plexhost + "\nServer may be offline, or token may be invalid.")
        print(e)