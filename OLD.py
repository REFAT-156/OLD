import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from OLD64 import bye
 
        bye()
 
 
 
elif bit == "32bit":
 
        from OLD32 import bye
 
 
        bye()
 
 
