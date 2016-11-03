#! /usr/bin/python2
# -*- coding: utf-8 -*-
import sys

def run(cmd):
    import os
    import sys
    from subprocess import Popen, PIPE
    print(cmd)
    proc=Popen(cmd, stdin=None, stdout=PIPE, stderr=None, shell=True)
    while True:
        data = proc.stdout.readline()   # Alternatively proc.stdout.read(1024)
        if len(data) == 0:
            print("Finished process")
            break
        sys.stdout.write(data)

import urllib

msg=sys.argv[1]
msg=urllib.quote_plus(msg)
# -v verbosity
cmd='curl '+ \
    '--output '+sys.argv[1]+'.mp3 '+ \
    "\""+'https://code.responsivevoice.org/develop/getvoice.php?t='+msg+'&tl=hi-US&sv=g2&vn=&pitch=0.5&rate=0.5&vol=1'+"\""+ \
    ' -H '+"\""+'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'+"\""+ \
    ' -H '+"\""+'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5'+"\""+ \
    ' -H '+"\""+'Accept-Language: pl,en-US;q=0.7,en;q=0.3'+"\""+ \
    ' -H '+"\""+'Range: bytes=0-'+"\""+ \
    ' -H '+"\""+'Referer: http://code.responsivevoice.org/develop/examples/example2.html'+"\""+ \
    ' -H '+"\""+'Cookie: __cfduid=ac862i73b6a61bf50b66713fdb4d9f62c1454856476; _ga=GA1.2.2126195996.1454856480; _gat=1'+"\""+ \
    ' -H '+"\""+'Connection: keep-alive'+"\""+ \
    ''
print('***************************')
print(cmd)
print('***************************')
run(cmd)
