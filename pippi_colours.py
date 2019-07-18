
#############################################################
# pippi: parse it, plot it
# ------------------------
# Colour scheme module for pippi.  Add your own at the end of
# this file.
#
# Author: Pat Scott (patscott@physics.mcgill.ca)
# Originally developed: March 2012
#############################################################

import re
import copy

permittedSchemes = {}

def Blockshading(colour,line_code, fill_code):
  scheme = colourScheme('Blockshading_'+colour)
  scheme.baseProfColourMap = '#fff--#fff(contour1)--#'+fill_code+'(contour1)--#'+fill_code
  scheme.basePostColourMap = '#fff--#fff(contour1)--#'+fill_code+'(contour1)--#'+fill_code
  scheme.mainPostContourColour2D = '\'#'+line_code+'\''
  scheme.mainProfContourColour2D = '\'#'+line_code+'\''
  scheme.mainBestFitColour1D = '#'+line_code
  scheme.mainPostMeanColour1D = '#'+line_code
  scheme.mainBestFitColour2D = '#'+line_code
  scheme.mainPostMeanColour2D = '#'+line_code
  scheme.fillTransparency2D = '0.85' #so far this is not actually functional in ctioga2; presumably it will work in later versions.
  return scheme


class colourScheme:
  # Class for pippi plotting colour schemes

  # Name of colour scheme
  name = ''

  # Default values for colours
  mainPostColour1D = 'Blue'
  mainProfColour1D = 'Red'
  mainPostContourColour2D = 'Black'
  mainProfContourColour2D = 'Black'
  comparisonPostColour1D = 'Grey'
  comparisonProfColour1D = 'Grey'
  comparisonPostContourColour2D = 'Grey'
  comparisonProfContourColour2D = 'Grey'

  comparison2PostColour1D = 'Grey'
  comparison2ProfColour1D = 'Grey'

  comparison2PostContourColour2D = 'Black'
  comparison2ProfContourColour2D = 'Grey'

  baseProfColourMap = '#fff--#fff(contour2)--#f45(contour1)--#612'
  basePostColourMap = '#fff--#fff(contour2)--#88f(contour1)--#229'

  # Default values for 1D plotting styles
  fillTransparency1D = '0.85'
  main1DLineStyle = 'Solid'
  comparison1DLineStyle = 'Solid' #alt: 'Dots', 'Dashes'
  comparison21DLineStyle = 'Solid' #alt: 'Dots', 'Dashes'
  
  lineWidth1D = '0.9'

  # Default values for 2D contour plotting styles
  fillTransparency2D = '1.0'
  mainContourStyle = 'Solid'
  secondaryContourStyle = 'Dashes'
  comparisonContourStyle = 'Dashes'
  comparison2ContourStyle = 'Dots'

  lineWidth2D = '0.9'

  # Default text and axis colours
  legendTextColour1D = 'Black'
  keyTextColour1D = 'Black'
  axisColour1D = 'Black'
  legendTextColour2D = 'Black'
  keyTextColour2D = 'Black'
  axisColour2D = 'Black'

  # Default markers and their colours
  referenceMarkerInner = 'Cross'
  referenceMarkerInnerScale = 0.7
  referenceMarkerInnerColour = 'Black'
  referenceMarkerOuter = 'Times'
  referenceMarkerOuterScale = 0.7
  referenceMarkerOuterColour = 'Yellow'

  mainBestFitMarker = 'Star'
  mainBestFitMarkerScale = 0.8
  mainBestFitColour1D = '#300'
  mainBestFitColour2D = 'Grey'
  mainBestFitColourOutline2D = 'Grey'

  mainPostMeanMarker = 'Bullet'
  mainPostMeanMarkerScale = 0.6
  mainPostMeanColour1D = '#004'
  mainPostMeanColour2D = '#004'
  mainPostMeanColourOutline2D = 'Grey'

  comparisonBestFitMarker = 'Star'
  comparisonBestFitMarkerScale = 0.8
  comparisonBestFitColour = 'Black'
  comparisonBestFitColourOutline2D = 'Black'

##################################################
  comparison2BestFitMarker = 'Star'
  comparison2BestFitMarkerScale = 0.8
  comparison2BestFitColour = 'Orange'
  comparison2BestFitColourOutline2D = 'Orange'
  

  comparisonPostMeanMarker = 'Bullet'
  comparisonPostMeanMarkerScale = 0.6
  comparisonPostMeanColour = 'Black'


  comparison2PostMeanMarker = 'Bullet'
  comparison2PostMeanMarkerScale = 0.6
  comparison2PostMeanColour = 'Orange'

  def __init__(self,name):
    global permittedSchemes
    name = name.lower()
    self.name = name
    if permittedSchemes is None:
      permittedSchemes = {name:self}
    else:
      permittedSchemes[name] = self

  def colourMap(self,contours,kind):
    #Construct colourmap from base colour map and contour levels
    if kind == 'post':
      localColourMap = self.basePostColourMap
    elif kind == 'like':
      localColourMap = self.baseProfColourMap
    else:
      sys.exit('    Error: unrecognised type of colourmap requested.\n    Quitting...\n')
    for i, contour in enumerate(contours):
      localColourMap = re.sub(r'contour'+str(i+1), contour, localColourMap)
    return localColourMap

# basic colour scheme
basic = colourScheme('basic')

# iceCube colour scheme
iceCube = colourScheme('iceCube')
iceCube.baseProfColourMap = '#fff--#fff(contour2)--#292(contour1)--#f55(contour1)--#000'
iceCube.basePostColourMap = '#fff--#fff(contour2)--#29d(contour1)--#f55(contour1)--#000'
iceCube.mainBestFitColour1D = 'Black'
iceCube.mainPostMeanColour1D = 'Black'
iceCube.mainBestFitColour2D = 'Black'
iceCube.mainPostMeanColour2D = 'Black'

# iceCube79 colour scheme
iceCube79 = colourScheme('iceCube79')
iceCube79.baseProfColourMap = '#fff--#fff(contour2)--#fab(contour1)--#f45'
iceCube79.basePostColourMap = '#fff--#fff(contour2)--#ddf(contour1)--#88f'
iceCube79.mainBestFitColour1D = 'Black'
iceCube79.mainPostMeanColour1D = 'Black'
iceCube79.mainBestFitColour2D = 'Black'
iceCube79.mainPostMeanColour2D = 'Black'
iceCube79.mainPostContourColour2D = 'Grey'
iceCube79.mainProfContourColour2D = 'Grey'
iceCube79.lineWidth2D = '1.5'

# iceCube3sig colour scheme
iceCube3sig = colourScheme('iceCube3sig')
iceCube3sig.baseProfColourMap = '#fff--#fff(contour3)--#292(contour2)--#fff(contour2)--#929(contour1)--#f55(contour1)--#000'
iceCube3sig.basePostColourMap = '#fff--#fff(contour3)--#29d(contour2)--#fff(contour2)--#929(contour1)--#f55(contour1)--#000'
iceCube3sig.mainBestFitColour1D = 'Black'
iceCube3sig.mainPostMeanColour1D = 'Black'
iceCube3sig.mainBestFitColour2D = 'Black'
iceCube3sig.mainPostMeanColour2D = 'Black'

# SBClassic colour scheme
SBClassic = colourScheme('SBClassic')
SBClassic.baseProfColourMap = '#fff--#fff(contour2)--#2f2(contour1)--#f33(0.5)--#000'
SBClassic.basePostColourMap = '#fff--#fff(contour2)--#95d(contour1)--#f33(0.5)--#000'
SBClassic.mainBestFitColour1D = 'Black'
SBClassic.mainPostMeanColour1D = 'Black'
SBClassic.mainBestFitColour2D = 'Black'
SBClassic.mainPostMeanColour2D = 'Black'

# BlueGold colour scheme
BlueGold = colourScheme('BlueGold')
BlueGold.baseProfColourMap = '#fff--#fff(contour2)--#f44(contour2)--#f44(contour1)--#ece(contour1)--#ece'
BlueGold.basePostColourMap = '#fff--#fff(contour2)--#44f(contour2)--#44f(contour1)--#fc0(contour1)--#fc0'
BlueGold.mainPostContourColour2D = 'DarkBlue'
BlueGold.mainProfContourColour2D = 'Maroon'
BlueGold.mainBestFitColour = 'Black'
BlueGold.mainBestFitColour1D = 'Black'
BlueGold.mainPostMeanColour1D = 'Black'
BlueGold.mainBestFitColour2D = 'Black'
BlueGold.mainPostMeanColour2D = 'Black'

# nightOfTheAllanachs colour scheme
nightOfTheAllanachs = colourScheme('nightOfTheAllanachs')
nightOfTheAllanachs.basePostColourMap = '#000--#000(contour2)--#808(contour1)--#f33(0.5)--#ff0'
nightOfTheAllanachs.baseProfColourMap = '#000--#000(contour2)--#33f(contour1)--#0ff(0.5)--#ff0'
nightOfTheAllanachs.mainPostContourColour2D = 'White'
nightOfTheAllanachs.mainProfContourColour2D = 'White'
nightOfTheAllanachs.axisColour2D = 'White'
nightOfTheAllanachs.mainBestFitColour1D = 'Black'
nightOfTheAllanachs.mainPostMeanColour1D = 'Black'
nightOfTheAllanachs.mainBestFitColour2D = 'White'
nightOfTheAllanachs.mainPostMeanColour2D = 'White'
nightOfTheAllanachs.legendTextColour2D = 'White'
nightOfTheAllanachs.keyTextColour2D = 'White'

# nightOfTheAllanachs2 colour scheme
nightOfTheAllanachs2 = colourScheme('nightOfTheAllanachs2')
nightOfTheAllanachs2.basePostColourMap = '#000--#000(contour2)--#808(contour1)--#f33(0.5)--#ff0'
nightOfTheAllanachs2.baseProfColourMap = '#000--#000(contour2)--#33f(contour1)--#0ff(0.5)--#ff0'
nightOfTheAllanachs2.mainPostContourColour2D = 'White'
nightOfTheAllanachs2.mainProfContourColour2D = 'White'
nightOfTheAllanachs2.axisColour2D = 'White'
nightOfTheAllanachs2.mainBestFitColour1D = 'Red'
nightOfTheAllanachs2.mainPostMeanColour1D = 'Blue'
nightOfTheAllanachs2.mainBestFitColour2D = 'White'
nightOfTheAllanachs2.mainBestFitColourOutline2D = 'Black'
nightOfTheAllanachs2.mainPostMeanColour2D = 'White'
nightOfTheAllanachs2.mainPostMeanColourOutline2D = 'Black'
nightOfTheAllanachs2.legendTextColour2D = 'White'
nightOfTheAllanachs2.keyTextColour2D = 'White'

# Blockshading colour schemes
Blockshading_red = Blockshading("red", "800", "e00")
Blockshading_green = Blockshading("green", "080", "0e0")
Blockshading_blue = Blockshading("blue", "005", "44f")
Blockshading_pink = Blockshading("pink", "808", "e0e")
Blockshading_purple = Blockshading("purple", "303", "80e")
Blockshading_orange = Blockshading("orange", "840", "f90")
Blockshading_yellow = Blockshading("yellow", "870", "fe0")
Blockshading_cyan = Blockshading("cyan", "088", "3ee")

# Multi-hue colour scheme (Added by Ankit Beniwal)
# Based on http://colorbrewer2.org/#type=sequential&scheme=GnBu&n=8
MultiHue = colourScheme('MultiHue')
MultiHue.basePostColourMap = '#FFFFFF--#edf8fb--#b3cde3--#8c96c6--#88419d'
MultiHue.baseProfColourMap = '#FFFFFF--#f0f9e8--#bae4bc--#7bccc4--#2b8cbe'
MultiHue.mainPostContourColour2D = 'Grey'
MultiHue.mainProfContourColour2D = 'Grey'
MultiHue.axisColour2D = 'Grey'
MultiHue.mainBestFitColour1D = 'Grey'
MultiHue.mainPostMeanColour1D = 'Grey'
MultiHue.mainPostMeanColour2D = 'Grey'
MultiHue.legendTextColour2D = 'Grey'
MultiHue.keyTextColour2D = 'Black'
MultiHue.mainBestFitMarker = 'Star'
MultiHue.mainBestFitMarkerScale = 0.8
MultiHue.mainBestFitColour1D = '#300'
MultiHue.mainBestFitColour2D = 'Grey'
MultiHue.mainBestFitColourOutline2D = 'Grey'
MultiHue.mainPostMeanMarker = 'Star'
MultiHue.mainPostMeanMarkerScale = 0.6
MultiHue.mainPostMeanColour1D = '#004'
MultiHue.mainPostMeanColour2D = '#004'
MultiHue.mainPostMeanColourOutline2D = 'Grey'

#############################################################
# Comparrison 
MultiHue.comparisonBestFitMarker = 'Bullet'
MultiHue.comparisonBestFitMarkerScale = 0.8
MultiHue.comparisonBestFitColour2D = 'Black'
MultiHue.comparisonBestFitColourOutline2D = 'Black'
MultiHue.comparisonPostMarker = 'Bullet'
MultiHue.comparisonPostMarkerScale = 0.8
MultiHue.comparisonPostColour2D = 'Black'
MultiHue.comparisonPostColourOutline2D = 'Black'
MultiHue.comparisonPostContourColour2D = 'Black'
MultiHue.comparisonProfContourColour2D = 'Black'
MultiHue.comparisonPostMeanMarker = 'Bullet'
MultiHue.comparisonPostMeanMarkerScale = 0.6
MultiHue.comparisonPostMeanColour = 'Black'

#############################################################
# Second comparrison
MultiHue.comparison2PostMeanMarker = 'Diamond'
MultiHue.comparison2PostMeanMarkerScale = 0.6
MultiHue.comparison2PostMeanColour = 'Orange'
MultiHue.comparison2BestFitMarker = 'Diamond'
MultiHue.comparison2BestFitMarkerScale = 0.8
MultiHue.comparison2BestFitColour2D = 'Orange'
MultiHue.comparison2BestFitColourOutline2D = 'Orange'
MultiHue.comparison2PostMarker = 'Diamond'
MultiHue.comparison2PostMarkerScale = 0.8
MultiHue.comparison2PostColour2D = 'Orange'
MultiHue.comparison2PostColourOutline2D = 'Orange'
MultiHue.comparison2PostContourColour2D = 'Orange'
MultiHue.comparison2ProfContourColour2D = 'Orange'
#ffffcc','#a1dab4','#41b6c4','#2c7fb8','#253494']

#############################################################
#############################################################
# Multi-hue variant colour scheme (Added by Andre)
MultiHueV = colourScheme('MultiHueV')
MultiHueV.basePostColourMap = '#FFFFFF--#edf8fb--#b3cde3--#8c96c6--#88419d'
MultiHueV.baseProfColourMap = '#FFFFFF--#f0f9e8--#bae4bc--#7bccc4--#2b8cbe'
MultiHueV.mainPostContourColour2D = 'Grey'
MultiHueV.mainProfContourColour2D = 'Grey'
MultiHueV.axisColour2D = 'Grey'
MultiHueV.mainBestFitColour1D = 'Grey'
MultiHueV.mainPostMeanColour1D = 'Grey'
MultiHueV.mainPostMeanColour2D = 'Grey'
MultiHueV.legendTextColour2D = 'Grey'
MultiHueV.keyTextColour2D = 'Black'
MultiHueV.mainBestFitMarker = 'Star'
MultiHueV.mainBestFitMarkerScale = 0.8
MultiHueV.mainBestFitColour1D = '#300'
MultiHueV.mainBestFitColour2D = 'Red'
MultiHueV.mainBestFitColourOutline2D = 'Red'
MultiHueV.mainPostMeanMarker = 'Star'
MultiHueV.mainPostMeanMarkerScale = 0.6
MultiHueV.mainPostMeanColour1D = '#004'
MultiHueV.mainPostMeanColour2D = '#004'
MultiHueV.mainPostMeanColourOutline2D = 'Grey'
#############################################################
# Comparrison 
MultiHueV.comparisonBestFitMarker = 'Bullet'
MultiHueV.comparisonBestFitMarkerScale = 0.8
MultiHueV.comparisonBestFitColour2D        = 'Orange'
MultiHueV.comparisonBestFitColourOutline2D = 'Orange'
MultiHueV.comparisonProfContourColour2D    = 'Orange'
MultiHueV.comparisonPostMarker = 'Bullet'
MultiHueV.comparisonPostMarkerScale = 0.8
MultiHueV.comparisonPostColour2D = 'Black'
MultiHueV.comparisonPostColourOutline2D = 'Black'
MultiHueV.comparisonPostContourColour2D = 'Black'
MultiHueV.comparisonPostMeanMarker = 'Bullet'
MultiHueV.comparisonPostMeanMarkerScale = 0.6
MultiHueV.comparisonPostMeanColour = 'Black'
#############################################################
# Second comparrison
MultiHueV.comparison2PostMeanMarker = 'Diamond'
MultiHueV.comparison2PostMeanMarkerScale = 0.6
MultiHueV.comparison2PostMeanColour = 'Orange'
MultiHueV.comparison2BestFitMarker = 'Diamond'
MultiHueV.comparison2BestFitMarkerScale = 0.8
MultiHueV.comparison2BestFitColour2D = 'Orange'
MultiHueV.comparison2BestFitColourOutline2D = 'Orange'
MultiHueV.comparison2PostMarker = 'Diamond'
MultiHueV.comparison2PostMarkerScale = 0.8
MultiHueV.comparison2PostColour2D = 'Orange'
MultiHueV.comparison2PostColourOutline2D = 'Orange'
MultiHueV.comparison2PostContourColour2D = 'Orange'
MultiHueV.comparison2ProfContourColour2D = 'Orange'
#############################################################
# Secondary contours
MultiHueV.mainContourStyle = 'Solid'
MultiHueV.secondaryContourStyle = 'Dashes'
MultiHueV.comparisonContourStyle = 'Solid'
MultiHueV.comparison2ContourStyle = 'Dots'
MultiHueV.lineWidth2D = '1.1'


# COlour mutihue2
# MultiHue2 colour scheme (Added by A. Beniwal)
MultiHue2 = colourScheme('MultiHue2')
MultiHue2.basePostColourMap = '#FFFFFF--#fdd49e--#fdbb84--#fc8d59--#e34a33--#b30000'
MultiHue2.baseProfColourMap = '#FFFFFF--#ccebc5--#a8ddb5--#7bccc4--#43a2ca--#0868ac'
MultiHue2.mainPostContourColour2D = 'Grey'
MultiHue2.mainProfContourColour2D = 'Grey'
MultiHue2.axisColour2D = 'Black'
MultiHue2.mainBestFitColour1D = 'Black'
MultiHue2.mainPostMeanColour1D = 'Black'
MultiHue2.mainBestFitColour2D = 'Red'
MultiHue2.mainPostMeanColour2D = 'Black'
MultiHue2.legendTextColour2D = 'Black'
MultiHue2.keyTextColour2D = 'Black'