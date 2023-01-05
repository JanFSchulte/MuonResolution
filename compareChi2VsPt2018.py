from ROOT import *
import pickle
import math
from setTDRStyle import setTDRStyle

ptbins = [52, 72, 100, 152, 200, 300, 452, 800.]


def efficiencyRatio(eff1,eff2):
	newEff = TGraphAsymmErrors(eff1.GetN())
	for i in range(0,eff1.GetN()):
		pointX1 = Double(0.)
		pointX2 = Double(0.)
		pointY1 = Double(0.)
		pointY2 = Double(0.)
		
		isSuccesful1 = eff1.GetPoint(i,pointX1,pointY1)
		isSuccesful2 = eff2.GetPoint(i,pointX2,pointY2)
		errY1Up = eff1.GetErrorYhigh(i)
		errY1Low = eff1.GetErrorYlow(i)
		errY2Up = eff2.GetErrorYhigh(i)
		errY2Low = eff2.GetErrorYlow(i)
		
		errX = eff1.GetErrorX(i)
		
		
		if pointY2!=0:
			yValue = pointY1/pointY2
			xValue = pointX1
			xError = errX
			#~ yErrorUp = math.sqrt(((1/pointY2)*errY1Up)**2+((pointY1/pointY2**2)*errY2Up)**2)
			yErrorUp = math.sqrt(((1/pointY2)*errY1Up)**2+((pointY1/pointY2**2)*errY2Up)**2)
			yErrorDown = math.sqrt(((1/pointY2)*errY1Low)**2+((pointY1/pointY2**2)*errY2Low)**2)				
		else:
			yValue = 0
			xValue = pointX1
			xError = errX
			yErrorUp =0
			yErrorDown = 0
			
		#~ print i
		newEff.SetPoint(i,xValue,yValue)
		newEff.SetPointError(i,xError,xError,yErrorDown,yErrorUp)
		
	return newEff
	
def getRatio(result,result2,label,Data=False):
	
	
	ptda = result["ptda"]
	ptda2   = result2["ptda"]

	if Data:
		sigma = result["da_nChi2"]
		sigma2 = result2["da_nChi2"]
	else:	
		sigma = result["mc_nChi2"]
		sigma2 = result2["mc_nChi2"]
	

	ratio  = TGraphAsymmErrors(len(ptda))
	ratio.SetName(label)
	for i,pt in enumerate(ptda):     
		ratio   .SetPoint(i,pt,sigma[i]/sigma2[i])
		ratio   .SetPointError(i,ptda[i]-ptbins[i],ptbins[i+1]-ptda[i],0,0)
	
	return ratio
	

def getGraph(result,label,Data=False):
	
	ptda = result["ptda"]

	if Data:
		sigma = result["da_nChi2"]
	else:	
		sigma = result["mc_nChi2"]
	sigmaErr = 0
	
	res  = TGraphAsymmErrors(len(ptda))
	res.SetName(label)
	for i,pt in enumerate(ptda):     
		res.SetPoint(i,pt,sigma[i])
		res.SetPointError(i,ptda[i]-ptbins[i],ptbins[i+1]-ptda[i],0,0)
	
	return res


def compareMassRes(trackType):
	
	file2016BB = open("2018BoosteddefaultLeadingGT36/MassResolutionVsPt_%s_Barrel.pkl"%trackType,"rb")
	file2016BE = open("2018BoosteddefaultLeadingGT36/MassResolutionVsPt_%s_OverlapEndcap.pkl"%trackType,"rb")
	file2017BB = open("2018BoostedcruijffLeading/MassResolutionVsPt_%s_Barrel.pkl"%trackType,"rb")
	file2017BE = open("2018BoostedcruijffLeading/MassResolutionVsPt_%s_OverlapEndcap.pkl"%trackType,"rb")
	file2018BB = open("2018BoostedcrystalLeading/MassResolutionVsPt_%s_Barrel.pkl"%trackType,"rb")
	file2018BE = open("2018BoostedcrystalLeading/MassResolutionVsPt_%s_OverlapEndcap.pkl"%trackType,"rb")

	results2016BB = pickle.load(file2016BB)
	results2016BE = pickle.load(file2016BE)
	results2017BB = pickle.load(file2017BB)
	results2017BE = pickle.load(file2017BE)
	results2018BB = pickle.load(file2018BB)
	results2018BE = pickle.load(file2018BE)

	graph2016BB = getGraph(results2016BB,"2016BB",Data=True)
	graph2016BE = getGraph(results2016BE,"2016BE",Data=True)
	graph2017BB = getGraph(results2017BB,"2017BB",Data=True)
	graph2017BE = getGraph(results2017BE,"2017BE",Data=True)
	graph2018BB = getGraph(results2018BB,"2018BB",Data=True)
	graph2018BE = getGraph(results2018BE,"2018BE",Data=True)
		
	
	ratioBB = 	getRatio(results2016BB,results2017BB,"ratioBB",Data=True)
	ratioBE = 	getRatio(results2016BE,results2017BE,"ratioBE",Data=True)



	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	#~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	#~ ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	#~ ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)

	xMax = 10
	if trackType == "Inner":
		xMax = 10
	if trackType == "Outer":
		xMax = 20

	plotPad.DrawFrame(0,0,800,xMax,";p_{T} [GeV]; #chi^{2}/N_{dof}")

	graph2016BB.Draw("samepe")
	graph2017BB.Draw("samepe")
	graph2018BB.Draw("samepe")
	graph2017BB.SetLineColor(kRed)
	graph2017BB.SetMarkerColor(kRed)
	graph2018BB.SetLineColor(kBlue)
	graph2018BB.SetMarkerColor(kBlue)

	latex = TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.055)
	latexCMS.SetNDC(True)
	latexCMSExtra = TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.03)
	latexCMSExtra.SetNDC(True) 

	latex.DrawLatex(0.95, 0.96, "(13 TeV)")

	cmsExtra = "#splitline{Preliminary}{}"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.84	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))			


	leg = TLegend(0.52, 0.76, 0.95, 0.91,"%s Central"%trackType,"brNDC")
	leg.SetFillColor(10)
	leg.SetFillStyle(0)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(graph2016BB,"Double-Sided CB","l")
	leg.AddEntry(graph2017BB,"Cruijff","l")
	leg.AddEntry(graph2018BB,"Crystal Ball","l")

	leg.Draw()

	plotPad.RedrawAxis()


	#~ ratioPad.cd()

	#~ ratioBB.SetLineColor(kRed)

	#~ ratioPad.DrawFrame(0,0.5,6000,1.5,";;ratio")

	#~ ratioBB.Draw("samepe")


	canv.Print("chi2CompareVsPt2018_%s_Central.pdf"%trackType)
	
	
	canv = TCanvas("c1","c1",800,800)

	plotPad = TPad("plotPad","plotPad",0,0,1,1)
	#~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	#~ ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	#~ ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)

	xMax = 10
	if trackType == "Inner":
		xMax = 10
	if trackType == "Outer":
		xMax = 10

	plotPad.DrawFrame(0,0,500,xMax,";p_{T} [GeV]; #chi^{2}/N_{dof}")

	graph2016BE.Draw("samepe")
	graph2017BE.Draw("samepe")
	graph2018BE.Draw("samepe")
	graph2017BE.SetLineColor(kRed)
	graph2017BE.SetMarkerColor(kRed)
	graph2018BE.SetLineColor(kBlue)
	graph2018BE.SetMarkerColor(kBlue)

	latex = TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.055)
	latexCMS.SetNDC(True)
	latexCMSExtra = TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.03)
	latexCMSExtra.SetNDC(True) 

	latex.DrawLatex(0.95, 0.96, "(13 TeV)")

	cmsExtra = "#splitline{Preliminary}{}"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.84	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))			


	leg = TLegend(0.52, 0.76, 0.95, 0.91,"%s Forward"%trackType,"brNDC")
	leg.SetFillColor(10)
	leg.SetFillStyle(0)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(graph2016BE,"Double-Sided CB","l")
	leg.AddEntry(graph2017BE,"Cruiff","l")
	leg.AddEntry(graph2018BE,"Crystal Ball","l")

	leg.Draw()

	plotPad.RedrawAxis()



	canv.Print("chi2CompareVsPt2018_%s_Forward.pdf"%trackType)


#~ tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]
for trackType in tracks:
	compareMassRes(trackType)
