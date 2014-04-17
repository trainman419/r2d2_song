#!/usr/bin/env python

import urllib

def main():
    post_url = 'http://www.r2d2translator.com/composeSongD2R2.php'
    for i in range(256):
        print i
        data = urllib.urlencode({'volumes': '1', 'sons': i})
        response = urllib.urlopen(post_url, data)
        audio_file = response.read()
        print audio_file
        audio_file = audio_file.partition('=')[2]
        print audio_file
        audio_url = "http://www.r2d2translator.com/audio/%s.MP3" % audio_file
        print audio_url
        response = urllib.urlopen(audio_url)
        audio_data = response.read()
        fname = "%d.mp3" % ( i )
        print "Saving to %s" % fname
        with open(fname, 'wb') as mp3:
            mp3.write(audio_data)

if __name__ == '__main__':
    main()
