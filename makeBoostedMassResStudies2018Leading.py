import subprocess

# ~ tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]

for track in tracks:

	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoosteddefaultLeadingGT36","--weight","True","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018.root","--iMC","2018PtBinned","-o","2018BoosteddefaultLeading","--weight","True","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedcrystalLeading","--weight","True","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedcruijffLeading","--weight","True","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin2Leading","--weight","True","--rebin","2","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin2CruijffLeading","--weight","True","--rebin","2","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin2CrystalLeading","--weight","True","--rebin","2","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin4Leading","--weight","True","--rebin","4","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin4CruijffLeading","--weight","True","--rebin","4","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedRebin4CrystalLeading","--weight","True","--rebin","4","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowSmallLeading","--weight","True","--xMin","80","--xMax","100","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowSmallCruijffLeading","--weight","True","--xMin","80","--xMax","100","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowSmallCrystalLeading","--weight","True","--xMin","800","--xMax","100","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowLargeLeading","--weight","True","--xMin","60","--xMax","120","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowLargeCruijffLeading","--weight","True","--xMin","60","--xMax","120","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2018_GT36.root","--iMC","2018PtBinned","-o","2018BoostedWindowLargeCrystalLeading","--weight","True","--xMin","60","--xMax","120","-f","CB","-t","%s"%track]
	subprocess.call(command)
