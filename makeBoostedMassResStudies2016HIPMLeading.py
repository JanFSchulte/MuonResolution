import subprocess

# ~ tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]

for track in tracks:

	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoosteddefaultLeading","--weight","True","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedcrystalLeading","--weight","True","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedcruijffLeading","--weight","True","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin2Leading","--weight","True","--rebin","2","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin2CruijffLeading","--weight","True","--rebin","2","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin2CrystalLeading","--weight","True","--rebin","2","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin4Leading","--weight","True","--rebin","4","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin4CruijffLeading","--weight","True","--rebin","4","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedRebin4CrystalLeading","--weight","True","--rebin","4","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowSmallLeading","--weight","True","--xMin","80","--xMax","100","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowSmallCruijffLeading","--weight","True","--xMin","80","--xMax","100","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowSmallCrystalLeading","--weight","True","--xMin","800","--xMax","100","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowLargeLeading","--weight","True","--xMin","60","--xMax","120","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowLargeCruijffLeading","--weight","True","--xMin","60","--xMax","120","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016HIPM.root","--iMC","2016HIPMPtBinned","-o","2016HIPMBoostedWindowLargeCrystalLeading","--weight","True","--xMin","60","--xMax","120","-f","CB","-t","%s"%track]
	subprocess.call(command)
