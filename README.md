**fb_bible.py v1.0**
_copyright Aaron Nelson 2017 (aaron.nelson805@gmail.com)_

FB_Bible is a python3 app that will post the entire Bible from Genesis to Revelations every hour (can be changed). If the script stops then it will pick up where it left off, rather than start over from the beginning.
**USAGE:**
 - You will have to obtain a Facebook OAUTH Token (https://developers.facebook.com/docs/pages/getting-started). Future releases will provide a method for automatic token generation. Once you have your FB Token (note: if posting to a page you will need to obtain the page ID also), enter the values in the provided in a file names 'apikeys' in your fb__bible directory. then enter your key in this format: `{'personal':'your facebook token here'}`
 - Enter a crontab entry for _fb__bible.py_ (to have it startup at boot enter _@reboot ~/path/to/fb__bible.py_
 - Start the script from command line: `$>./fb_bible &`
 
