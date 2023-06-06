import subprocess

# ~ tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]

for track in tracks:

	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoosteddefaultLeading","--weight","True","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedcrystalLeading","--weight","True","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedcruijffLeading","--weight","True","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin2Leading","--weight","True","--rebin","2","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin2CruijffLeading","--weight","True","--rebin","2","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin2CrystalLeading","--weight","True","--rebin","2","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin4Leading","--weight","True","--rebin","4","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin4CruijffLeading","--weight","True","--rebin","4","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedRebin4CrystalLeading","--weight","True","--rebin","4","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowSmallLeading","--weight","True","--xMin","80","--xMax","100","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowSmallCruijffLeading","--weight","True","--xMin","80","--xMax","100","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowSmallCrystalLeading","--weight","True","--xMin","800","--xMax","100","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowLargeLeading","--weight","True","--xMin","60","--xMax","120","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowLargeCruijffLeading","--weight","True","--xMin","60","--xMax","120","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2016.root","--iMC","2016PtBinned","-o","2016BoostedWindowLargeCrystalLeading","--weight","True","--xMin","60","--xMax","120","-f","CB","-t","%s"%track]
	subprocess.call(command)
