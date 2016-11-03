#! /usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import os
from subprocess import Popen, PIPE

def run(cmd):
    proc=Popen(cmd, stdin=None, stdout=PIPE, stderr=None, shell=True)
    while True:
        data = proc.stdout.readline()   # Alternatively proc.stdout.read(1024)
        if len(data) == 0:
            print("Finished process")
            break
        sys.stdout.write(data)

import urllib

def get(num):
	msg=`num`
	print "Downloading : " + msg
	msg=urllib.quote_plus(msg)
	dirpath="./lang/"+sys.argv[1]+"/"
	# -v verbosity
	cmd='curl '+ \
		'--output '+dirpath+`num`+'.mp3 '+ \
		"\""+'https://code.responsivevoice.org/develop/getvoice.php?t='+msg+'&tl='+sys.argv[1]+'&sv=g2&vn=&pitch=0.5&rate=0.5&vol=1'+"\""+ \
		' -H '+"\""+'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'+"\""+ \
		' -H '+"\""+'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5'+"\""+ \
		' -H '+"\""+'Accept-Language: pl,en-US;q=0.7,en;q=0.3'+"\""+ \
		' -H '+"\""+'Range: bytes=0-'+"\""+ \
		' -H '+"\""+'Referer: http://code.responsivevoice.org/develop/examples/example2.html'+"\""+ \
		' -H '+"\""+'Cookie: __cfduid=ac862i73b6a61bf50b66713fdb4d9f62c1454856476; _ga=GA1.2.2126195996.1454856480; _gat=1'+"\""+ \
		' -H '+"\""+'Connection: keep-alive'+"\""+ \
		''
	run(cmd)
	os.system("mpg123 -w "+dirpath+`num`+".wav "+dirpath+`num`+".mp3") 
	os.system("rm "+dirpath+`num`+".mp3")

count = float(sys.argv[2])
os.system('mkdir ./lang/'+sys.argv[1])
while count<= float(sys.argv[3]):
	get(count)
	count += float(sys.argv[4])
msg = "degree celsius"
msg=urllib.quote_plus(msg)
dirpath="./lang/"+sys.argv[1]+"/"
# -v verbosity
cmd='curl '+ \
	'--output '+dirpath+'degree_celsius.mp3 '+ \
	"\""+'https://code.responsivevoice.org/develop/getvoice.php?t='+msg+'&tl='+sys.argv[1]+'&sv=g2&vn=&pitch=0.5&rate=0.5&vol=1'+"\""+ \
	' -H '+"\""+'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'+"\""+ \
	' -H '+"\""+'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5'+"\""+ \
	' -H '+"\""+'Accept-Language: pl,en-US;q=0.7,en;q=0.3'+"\""+ \
	' -H '+"\""+'Range: bytes=0-'+"\""+ \
	' -H '+"\""+'Referer: http://code.responsivevoice.org/develop/examples/example2.html'+"\""+ \
	' -H '+"\""+'Cookie: __cfduid=ac862i73b6a61bf50b66713fdb4d9f62c1454856476; _ga=GA1.2.2126195996.1454856480; _gat=1'+"\""+ \
	' -H '+"\""+'Connection: keep-alive'+"\""+ \
	''
run(cmd)
os.system("mpg123 -w "+dirpath+"degree_celsius.wav "+dirpath+"degree_celsius.mp3") 
os.system("rm "+dirpath+"degree_celsius.mp3")	

msg = "minus"
msg=urllib.quote_plus(msg)
dirpath="./lang/"+sys.argv[1]+"/"
# -v verbosity
cmd='curl '+ \
	'--output '+dirpath+'minus.mp3 '+ \
	"\""+'https://code.responsivevoice.org/develop/getvoice.php?t='+msg+'&tl='+sys.argv[1]+'&sv=g2&vn=&pitch=0.5&rate=0.5&vol=1'+"\""+ \
	' -H '+"\""+'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'+"\""+ \
	' -H '+"\""+'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5'+"\""+ \
	' -H '+"\""+'Accept-Language: pl,en-US;q=0.7,en;q=0.3'+"\""+ \
	' -H '+"\""+'Range: bytes=0-'+"\""+ \
	' -H '+"\""+'Referer: http://code.responsivevoice.org/develop/examples/example2.html'+"\""+ \
	' -H '+"\""+'Cookie: __cfduid=ac862i73b6a61bf50b66713fdb4d9f62c1454856476; _ga=GA1.2.2126195996.1454856480; _gat=1'+"\""+ \
	' -H '+"\""+'Connection: keep-alive'+"\""+ \
	''
run(cmd)
os.system("mpg123 -w "+dirpath+"minus.wav "+dirpath+"minus.mp3") 
os.system("rm "+dirpath+"minus.mp3")