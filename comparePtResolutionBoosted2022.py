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
	
def getGraph(result,label):
	
	ptda = result["ptda"]
	da_sig = result["data_sig"]
	da_sige = result["data_sige"]
	
	res_data  = TGraphAsymmErrors(len(ptda))
	res_data.SetName(label)
	for i,pt in enumerate(ptda):        
		res_data.SetPoint(i,ptda[i],da_sig[i])
		#~ print ptda[i],ptda[i]-ptbins[i],ptbins[i+1]-ptda[i]
		res_data.SetPointError(i,ptda[i]-ptbins[i],ptbins[i+1]-ptda[i],da_sige[i],da_sige[i])
	
	return res_data

def getRatio(result,result2,label):
	
	ptda = result["ptda"]
	da_sig = result["data_sig"]
	da_sige = result["data_sige"]
	ptmc = result2["ptda"]
	mc_sig = result2["data_sig"]
	mc_sige = result2["data_sige"]
	
	ratio  = TGraphAsymmErrors(len(ptda))
	ratio.SetName(label)
	for i,pt in enumerate(ptda):     
		#~ pt_e = (ptbins[i+1]-ptbins[i])/2   
		sig_e = (da_sig[i]/mc_sig[i])*math.sqrt((da_sige[i]/da_sig[i])**2+(mc_sige[i]/mc_sig[i])**2)
		ratio   .SetPoint(i,pt,da_sig[i]/mc_sig[i])
		ratio   .SetPointError(i,ptda[i]-ptbins[i],ptbins[i+1]-ptda[i],sig_e,sig_e)
	
	return ratio



def comparePtRes(trackType):
	
	file2022B = open("2022BoosteddefaultLeading/MassResolutionVsPt_%s_Barrel.pkl"%trackType,"rb")
	file2022O = open("2022BoosteddefaultLeading/MassResolutionVsPt_%s_Overlap.pkl"%trackType,"rb")
	file2022E = open("2022BoosteddefaultLeading/MassResolutionVsPt_%s_OverlapEndcap.pkl"%trackType,"rb")
	file2018B = open("2018BoosteddefaultLeadingGT36/MassResolutionVsPt_%s_Barrel.pkl"%trackType,"rb")
	file2018O = open("2018BoosteddefaultLeadingGT36/MassResolutionVsPt_%s_Overlap.pkl"%trackType,"rb")
	file2018E = open("2018BoosteddefaultLeadingGT36/MassResolutionVsPt_%s_OverlapEndcap.pkl"%trackType,"rb")

	results2022B = pickle.load(file2022B)
	results2022O = pickle.load(file2022O)
	results2022E = pickle.load(file2022E)
	results2018B = pickle.load(file2018B)
	results2018O = pickle.load(file2018O)
	results2018E = pickle.load(file2018E)

	graph2022B = getGraph(results2022B,"2022B")
	graph2022O = getGraph(results2022O,"2022O")
	graph2022E = getGraph(results2022E,"2022E")
	graph2018B = getGraph(results2018B,"2018B")
	graph2018O = getGraph(results2018O,"2018O")
	graph2018E = getGraph(results2018E,"2018E")
		
	
	ratioB18 = getRatio(results2022B,results2018B,"ratioB18")
	ratioO18 = getRatio(results2022O,results2018O,"ratioO18")
	ratioE18 = getRatio(results2022E,results2018E,"ratioE18")



	canv = TCanvas("c1","c1",800,1200)

	plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)
	gStyle.SetTitleYOffset(1.55)

	xMax = 6
	if trackType == "Inner":
		xMax = 8
	if trackType == "Outer":
		xMax = 20

	plotPad.DrawFrame(52,0,800,xMax,";Leading muon p_{T} [GeV]; Z peak resolution [GeV]")

	graph2022B.Draw("samepe")
	graph2018B.Draw("samepe")
	graph2018B.Draw("samepe")
	graph2018B.SetLineColor(kBlue)
	graph2018B.SetMarkerColor(kBlue)

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

	latex.DrawLatex(0.95, 0.96, "(13 TeV, 13.6 TeV)")

	cmsExtra = "#splitline{Preliminary}{}"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.81	
	else:
		yLabelPos = 0.84	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))			


	leg = TLegend(0.52, 0.76, 0.95, 0.91,"%s |#eta| < 1.2"%trackType,"brNDC")
	leg.SetFillColor(10)
	leg.SetFillStyle(0)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(graph2022B,"2022 B-F","l")
	leg.AddEntry(graph2018B,"2018","l")

	leg.Draw()

	plotPad.RedrawAxis()


	ratioPad.cd()

	ratioB18.SetLineColor(kBlue)
	ratioB18.SetMarkerColor(kBlue)

	ratioPad.DrawFrame(52,0.5,800,1.5,";;ratio")

	ratioB18.Draw("samepe")

	l = TLine(52,1,800,1)
	l.SetLineStyle(kDashed)
	l.Draw()
	
	canv.Print("PtResolutionBoostedCompare2022_%s_B.pdf"%trackType)
	
	
	# ~ canv = TCanvas("c1","c1",800,1200)

	# ~ plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	# ~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	# ~ style = setTDRStyle()
	# ~ gStyle.SetOptStat(0)
	# ~ plotPad.UseCurrentStyle()
	# ~ ratioPad.UseCurrentStyle()
	# ~ plotPad.Draw()	
	# ~ ratioPad.Draw()	
	# ~ plotPad.cd()
	# ~ plotPad.cd()
	# ~ plotPad.SetGrid()
	# ~ gStyle.SetTitleXOffset(1.45)
	# ~ gStyle.SetTitleYOffset(1.55)

	# ~ xMax = 6
	# ~ if trackType == "Inner":
		# ~ xMax = 8
	# ~ if trackType == "Outer":
		# ~ xMax = 20

	# ~ plotPad.DrawFrame(52,0,452,xMax,";Leading muon p_{T} [GeV]; Z peak resolution [GeV]")

	# ~ graph2022O.Draw("samepe")
	# ~ graph2018O.Draw("samepe")
	# ~ graph2018O.SetLineColor(kBlue)
	# ~ graph2018O.SetMarkerColor(kBlue)

	# ~ latex = TLatex()
	# ~ latex.SetTextFont(42)
	# ~ latex.SetTextAlign(31)
	# ~ latex.SetTextSize(0.04)
	# ~ latex.SetNDC(True)
	# ~ latexCMS = TLatex()
	# ~ latexCMS.SetTextFont(61)
	# ~ latexCMS.SetTextSize(0.055)
	# ~ latexCMS.SetNDC(True)
	# ~ latexCMSExtra = TLatex()
	# ~ latexCMSExtra.SetTextFont(52)
	# ~ latexCMSExtra.SetTextSize(0.03)
	# ~ latexCMSExtra.SetNDC(True) 

	# ~ latex.DrawLatex(0.95, 0.96, "(13 TeV)")

	# ~ cmsExtra = "#splitline{Preliminary}{}"
	# ~ latexCMS.DrawLatex(0.19,0.88,"CMS")
	# ~ if "Simulation" in cmsExtra:
		# ~ yLabelPos = 0.81	
	# ~ else:
		# ~ yLabelPos = 0.84	

	# ~ latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))			


	# ~ leg = TLegend(0.52, 0.76, 0.95, 0.91,"%s 1.2 < |#eta| < 1.6"%trackType,"brNDC")
	# ~ leg.SetFillColor(10)
	# ~ leg.SetFillStyle(0)
	# ~ leg.SetLineColor(10)
	# ~ leg.SetShadowColor(0)
	# ~ leg.SetBorderSize(1)		
	# ~ leg.AddEntry(graph2022O,"2022 B-F","l")
	# ~ leg.AddEntry(graph2018O,"2018","l")

	# ~ leg.Draw()

	# ~ plotPad.RedrawAxis()


	# ~ ratioPad.cd()

	# ~ ratioO18.SetLineColor(kBlue)
	# ~ ratioO18.SetMarkerColor(kBlue)

	# ~ ratioPad.DrawFrame(52,0.5,452,1.5,";;ratio")

	# ~ l = TLine(52,1,452,1)
	# ~ l.SetLineStyle(kDashed)
	# ~ l.Draw()

	# ~ ratioO18.Draw("samepe")


	# ~ canv.Print("PtResolutionBoostedCompare2022_%s_O.pdf"%trackType)
	
	
	canv = TCanvas("c1","c1",800,1200)

	plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	plotPad.SetGrid()
	gStyle.SetTitleXOffset(1.45)
	gStyle.SetTitleYOffset(1.55)

	xMax = 6
	if trackType == "Inner":
		xMax = 8
	if trackType == "Outer":
		xMax = 20

	plotPad.DrawFrame(52,0,452,xMax,";Leading muon p_{T} [GeV]; Z peak resolution [GeV]")

	graph2022E.Draw("samepe")
	graph2018E.Draw("samepe")
	graph2018E.SetLineColor(kBlue)
	graph2018E.SetMarkerColor(kBlue)

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


	leg = TLegend(0.52, 0.76, 0.95, 0.91,"%s |#eta| > 1.2"%trackType,"brNDC")
	leg.SetFillColor(10)
	leg.SetFillStyle(0)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)
	leg.SetBorderSize(1)		
	leg.AddEntry(graph2022E,"2022 B-F","l")
	leg.AddEntry(graph2018E,"2018","l")

	leg.Draw()

	plotPad.RedrawAxis()


	ratioPad.cd()

	ratioO18.SetLineColor(kBlue)
	ratioO18.SetMarkerColor(kBlue)

	ratioPad.DrawFrame(52,0.5,452,1.5,";;ratio")

	l = TLine(52,1,452,1)
	l.SetLineStyle(kDashed)
	l.Draw()

	ratioE18.Draw("samepe")


	canv.Print("PtResolutionBoostedCompare2022_%s_OE.pdf"%trackType)


#tracks = ["Inner","Outer","Global","TPFMS","Picky","DYT","TunePNew"]
tracks = ["TunePNew"]
for trackType in tracks:
	comparePtRes(trackType)
