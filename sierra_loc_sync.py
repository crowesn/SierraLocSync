#expect_loc_sync.py
import getpass, re, sys, telnetlib, pexpect
from time import strftime
from time import sleep

#contants
SessionUser = '' #session username
SessionPass = '' #session password
initials = '' #optional generic SessionUser account, default blank
initpass = '' #optional generic SessionUser account pass, default blank
HOST = 'uclid.uc.edu'

print '......Loc Sync......\n\n'

def SessionLogin(sessionpass):#choose mil session; cat, acq, etc
  #write milcat login
  tn.expect('@uclid.uc.edu\'s password:')
  fout = file('mylog.txt','w')
  tn.logfile = fout
#  tn.logfile = sys.stdout  
  #get credentials and pass to server
  tn.send(sessionpass + "\n")
  tn.expect("Choose one")
  return

def Authenticate(initials, initpass):#autenticate with username and pass
  #check for generic account, if gen acc not present, prompt for auth
  if initials == '':
    initials = raw_input('please key your initials: ')
  tn.expect('Login:')
  tn.send(initials + '\n')
  #check for generic account, if gen acc not present, prompt for auth
  if initpass == '':
    initpass = getpass.getpass()
  if initpass:
    tn.expect('Password:')
    tn.send(initpass + '\n')
  return

#Connect to UCLID telnet and autheticate
tn = pexpect.spawn('ssh cat20@' + HOST)
tn.logfile = sys.stdout
SessionLogin(SessionPass)
sleep(5)
#Select 'create lists'
tn.send('a')
sleep(5)
tn.send('l')
sleep(5)
Authenticate(initials, initpass)

tn.expect('Choose one')

tn.send('u')
sleep(5)
tn.send('r')
sleep(5)

tn.send('10000008\n') #Enter a starting record
sleep(5)
tn.send('\n') #Enter ending record (key return to get highest number)
sleep(5)
tn.send('y') #Is this range correct?
sleep(5)
tn.send('a') #Choose type of record to be examined
sleep(5)
tn.send('y') #Begin Processing?
sleep(5)
tn.expect('Press <SPACE> to continue')
tn.send(chr(32))
sleep(5)
tn.send('qqqq')
#exit telnet

