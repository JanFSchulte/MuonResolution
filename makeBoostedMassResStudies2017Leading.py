import subprocess

# ~ tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]

for track in tracks:

	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoosteddefaultLeading","--weight","True","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedcrystalLeading","--weight","True","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedcruijffLeading","--weight","True","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin2Leading","--weight","True","--rebin","2","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin2CruijffLeading","--weight","True","--rebin","2","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin2CrystalLeading","--weight","True","--rebin","2","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin4Leading","--weight","True","--rebin","4","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin4CruijffLeading","--weight","True","--rebin","4","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedRebin4CrystalLeading","--weight","True","--rebin","4","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowSmallLeading","--weight","True","--xMin","80","--xMax","100","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowSmallCruijffLeading","--weight","True","--xMin","80","--xMax","100","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowSmallCrystalLeading","--weight","True","--xMin","800","--xMax","100","-f","CB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowLargeLeading","--weight","True","--xMin","60","--xMax","120","-f","doubleCB","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowLargeCruijffLeading","--weight","True","--xMin","60","--xMax","120","-f","cruijff","-t","%s"%track]
	subprocess.call(command)
	command = ["python","makeMassRes_atZLeading.py","--iDATA","data2017.root","--iMC","2017PtBinned","-o","2017BoostedWindowLargeCrystalLeading","--weight","True","--xMin","60","--xMax","120","-f","CB","-t","%s"%track]
	subprocess.call(command)
