#expect_loc_sync.py
import getpass, re, sys, telnetlib, pexpect
from time import strftime

#contants
SessionUser = '' #session username
SessionPass = '' #session password
initials = '' #optional generic SessionUser account, default blank
initpass = '' #optional generic SessionUser account pass, default blank
HOST = 'uclid.uc.edu'

print '......Loc Sync......\n\n'

def sessionlogin(sessionpass):#choose mil session; cat, acq, etc
  #write milcat login
  tn.expect('@uclid.uc.edu\'s password:')
  fout = file('mylog.txt','w')
  tn.logfile = fout
  tn.logfile = sys.stdout  
  #get credentials and pass to server
  tn.send(sessionpass + "\n")
  tn.expect("choose one")
  return

def authenticate(initials, initpass):#autenticate with username and pass
  #check for generic account, if gen acc not present, prompt for auth
  if initials == '':
    initials = raw_input('please key your initials: ')
  tn.expect('please key your initials : ')
  tn.send(initials + '\n')
  #check for generic account, if gen acc not present, prompt for auth
  if initpass == '':
    initpass = getpass.getpass()
  if initpass:
    tn.expect('please key your password : ')
    tn.send(initpass + '\n')
  return

#Connect to UCLID telnet and autheticate
tn = pexpect.spawn('ssh cat20@' + HOST)
tn.logfile = sys.stdout
SessionLogin(SessionPass)

#Select 'create lists'
tn.send('a')
tn.send('l')

Authenticate(initials, initpass)

tn.expect('Choose one')

tn.send('u')
tn.send('r')


tn.send('10000008\n') #Enter a starting record
tn.send('\n') #Enter ending record (key return to get highest number)
tn.send('y') #Is this range correct?
tn.send('a') #Choose type of record to be examined
tn.send('y') #Begin Processing?


tn.expect('Choose one')
#exit telnet
tn.send("qqqqqq")
print '\a\a\a'
raw_input("\nTitle Report Finished <Press ENTER>")

