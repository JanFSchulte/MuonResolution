import subprocess

command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","default2016HIPMP","-f","doubleCB"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","crystal2016HIPMP","-f","crystal"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","cruijff2016HIPMP"]
subprocess.call(command)
#~ command = ["python","makePRes.py","-i","2016MassBinned","-o","default2016","-f","doubleCB"]
#~ subprocess.call(command)
#~ command = ["python","makePRes.py","-i","2016MassBinned","-o","cruijff2016"]
#~ subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","Rebin22016HIPMP","--rebin","2","-f","doubleCB"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","Rebin82016HIPMP","--rebin","8","-f","doubleCB"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","Rebin22016HIPMCruijffP","--rebin","2"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","Rebin82016HIPMCruijffP","--rebin","8"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","WindowSmall2016HIPMP","--xMinFac","-1","--xMaxFac","1","-f","doubleCB"]
subprocess.call(command)
command = ["python","makePResSplit.py","-i","2016HIPMMassBinned","-o","WindowLarge2016HIPMP","--xMinFac","-2","--xMaxFac","2","-f","doubleCB"]
subprocess.call(command)
