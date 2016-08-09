import requests
import xml.etree.ElementTree as xml
import os


full = 'https://71-94-74-4.f7359db7e21248d3a778108b15dff67e.plex.direct:32400/hubs/search?query=%5Bunknown%20album%5D&limit=30&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x388%2C1920x1080&X-Plex-Token=9FDhRrsWszn2ogBVWU2o'
full = 'https://71-94-74-4.f7359db7e21248d3a778108b15dff67e.plex.direct:32400/library/metadata/1314/children?includeRelated=1&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x388%2C1920x1080&X-Plex-Token=9FDhRrsWszn2ogBVWU2o'

searchUrl = '/hubs/search?query=%5Bunknown%20album%5D&limit=30&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x388%2C1920x1080&X-Plex-Token='
accessPoint = 'http://71-94-74-4.f7359db7e21248d3a778108b15dff67e.plex.direct:32400'
token = '9FDhRrsWszn2ogBVWU2o'




unknownReq = accessPoint + searchUrl + token

unk = requests.get(unknownReq)

#print unk.content

albums = xml.fromstring(unk.content)


filepaths = []
for album in albums.iter('Directory'):
    
    #print album.get('ratingKey')
    
    albumUrl = accessPoint + '/library/metadata/' + album.get('ratingKey') + '/children?includeRelated=1&X-Plex-Product=Plex%20Web&X-Plex-Version=2.7.4&X-Plex-Client-Identifier=2i0z1w5wvq72wnwhpfhr02uik9&X-Plex-Platform=Chrome&X-Plex-Platform-Version=51.0&X-Plex-Device=Windows&X-Plex-Device-Name=Plex%20Web%20%28Chrome%29&X-Plex-Device-Screen-Resolution=1858x388%2C1920x1080&X-Plex-Token=' + token
    
    alb = requests.get(albumUrl)
    
    #print alb.content
    tracks = xml.fromstring(alb.content)
    for track in tracks.iter('Part'):
        fullpath = track.get('file')
        print fullpath
        
        filepaths.append(fullpath)
    
    #if True: break
    
for fp in filepaths:
    head, tail = os.path.split(fp)
    name, ext = os.path.splitext(tail)
    os.rename(fp, os.path.join(head, name + '#PLEX#' + ext))

raw_input('Update PLEX Library now')

for fp in filepaths:
    head, tail = os.path.split(fp)
    name, ext = os.path.splitext(tail)
    os.rename(os.path.join(head, name + '#PLEX#' + ext), fp)

