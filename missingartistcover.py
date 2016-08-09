import requests
import xml.etree.ElementTree as xml
import os


full = 'https://71-94-74-4.f7359db7e21248d3a778108b15dff67e.plex.direct:32400/library/sections/2/all?type=8&sort=titleSort%3Aasc&X-Plex-Container-Start=0&X-Plex-Container-Size=64&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x995%2C1920x1080&X-Plex-Token=9FDhRrsWszn2ogBVWU2o'

searchUrl = '/library/sections/2/all?type=8&sort=titleSort%3Aasc&X-Plex-Container-Start=0&X-Plex-Container-Size=64&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x995%2C1920x1080&X-Plex-Token='
accessPoint = 'http://71-94-74-4.f7359db7e21248d3a778108b15dff67e.plex.direct:32400'
token = '9FDhRrsWszn2ogBVWU2o'




unknownReq = accessPoint + searchUrl + token

unk = requests.get(unknownReq)

#print unk.content

artists = xml.fromstring(unk.content)


artistIds = []
for artist in artists.iter('Directory'):
    
    #print album.get('ratingKey')
    
    

