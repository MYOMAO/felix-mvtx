echo $1
ddump -s -g -n 0 -p 2001 $1  | ../decode.py -wpm -p 500000 -i 0
ddump -s -g -n 0 -p 2001 $1  | ../decode.py -wpm -p 500000 -i 256
ddump -s -g -n 0 -p 2001 $1  | ../decode.py -wpm -p 500000 -i 512
ddump -s -g -n 0 -p 2002 $1  | ../decode.py -wpm -p 500000 -i 4099
ddump -s -g -n 0 -p 2002 $1  | ../decode.py -wpm -p 500000 -i 4355
ddump -s -g -n 0 -p 2002 $1  | ../decode.py -wpm -p 500000 -i 4611
ddump -s -g -n 0 -p 2003 $1  | ../decode.py -wpm -p 500000 -i 8198
ddump -s -g -n 0 -p 2003 $1  | ../decode.py -wpm -p 500000 -i 8454
ddump -s -g -n 0 -p 2003 $1  | ../decode.py -wpm -p 500000 -i 8710
ddump -s -g -n 0 -p 2004 $1  | ../decode.py -wpm -p 500000 -i 8199
ddump -s -g -n 0 -p 2004 $1  | ../decode.py -wpm -p 500000 -i 8455
ddump -s -g -n 0 -p 2004 $1  | ../decode.py -wpm -p 500000 -i 8711
ddump -s -g -n 0 -p 2005 $1  | ../decode.py -wpm -p 500000 -i 1
ddump -s -g -n 0 -p 2005 $1  | ../decode.py -wpm -p 500000 -i 257
ddump -s -g -n 0 -p 2005 $1  | ../decode.py -wpm -p 500000 -i 513
ddump -s -g -n 0 -p 2006 $1  | ../decode.py -wpm -p 500000 -i 4100
ddump -s -g -n 0 -p 2006 $1  | ../decode.py -wpm -p 500000 -i 4356
ddump -s -g -n 0 -p 2006 $1  | ../decode.py -wpm -p 500000 -i 4612
ddump -s -g -n 0 -p 2007 $1  | ../decode.py -wpm -p 500000 -i 8200
ddump -s -g -n 0 -p 2007 $1  | ../decode.py -wpm -p 500000 -i 8456
ddump -s -g -n 0 -p 2007 $1  | ../decode.py -wpm -p 500000 -i 8712
ddump -s -g -n 0 -p 2008 $1  | ../decode.py -wpm -p 500000 -i 8201
ddump -s -g -n 0 -p 2008 $1  | ../decode.py -wpm -p 500000 -i 8457
ddump -s -g -n 0 -p 2008 $1  | ../decode.py -wpm -p 500000 -i 8713
