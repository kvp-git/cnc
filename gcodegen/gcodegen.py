from datetime import datetime

cncVarFeedRate = 20
cncVarMoveRate = 200
cncVarToolParkHeight = 1
cncVarToolLiftHeight = 10

def cncStr(n):
  return "{:.3f}".format(n)

def cncHeader():
  print("(cnc g code generator by kvp in 2024)")
  print("(" + datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + ")")
  print("G21 G17 G90 F100") # metric (1 mm unit)
  print("G10 P0 L20 X0 Y0 Z" + cncStr(cncVarToolParkHeight)) # reset coordinates
  print("G00 Z" + cncStr(cncVarToolLiftHeight) + " F" + cncStr(cncVarMoveRate)) # lift the tool from the calibration point

def cncPark():
  print("G01 Z" + cncStr(cncVarToolLiftHeight) + " F" + cncStr(cncVarFeedRate))
  print("G00 X0 Y0 F" + cncStr(cncVarMoveRate))
  print("G00 Z" + cncStr(cncVarToolParkHeight) +" F" + cncStr(cncVarMoveRate))

def cncSetFeedRate(feedRate):
  cncVarFeedrate = feedRate

def cncSetMoveRate(moveRate):
  cncVarMoveRate = moveRate

def cncSetToolLiftHeight(height):
  cncVarToolLiftHeight = height

def cncMoveTool(x, y):
  print("G00 X" + cncStr(x) + " Y" + cncStr(y) + " F" + cncStr(cncVarMoveRate))

def cncLowerTool(cutDepth):
  print("G01 Z0.1 F" + cncStr(cncVarMoveRate))
  print("G01 Z" + cncStr(-cutDepth) + " F" + cncStr(cncVarFeedRate))

def cncSinkTool(cutDepth):
  print("G01 Z" + cncStr(-cutDepth) + " F" + cncStr(cncVarFeedRate))

def cncLiftTool():
  print("G01 Z0.1 F" + cncStr(cncVarFeedRate))
  print("G01 Z" + cncStr(cncVarToolLiftHeight) + " F" + cncStr(cncVarMoveRate))

def cncWait(timeMsec):
  #print("G04 P" + cncStr(timeMsec)) TODO!!!
  pass

def cncDrill(x, y, cutDepth):
  cncMoveTool(x, y)
  cncLowerTool(cutDepth)
  cncLiftTool()

def cncCutPath(x, y):
  print("G01 X" + cncStr(x) + " Y" + cncStr(y) + " F" + cncStr(cncVarFeedRate))

def cncCutLine(x1, y1, x2, y2, cutDepth):
  cncMoveTool(x1, y1)
  cncLowerTool(cutDepth)
  cncCutPath(x2, y2)
  cncLiftTool()

def cncCutLines(points, cutDepth):
  cncMoveTool(points[0][0], points[0][1])
  cncLowerTool(cutDepth)
  for p in points:
    cncCutPath(p[0], p[1])
  cncLiftTool()

def cncCutInsideRectangle(x, y, width, height, toolWidth, cutDepth):
  x1 = x + (toolWidth / 2.0)
  y1 = y + (toolWidth / 2.0)
  x2 = x + width - (toolWidth / 2.0)
  y2 = y + height - (toolWidth / 2.0)
  cncMoveTool(x1, y1)
  cncLowerTool(cutDepth)
  print("G01 X" + cncStr(x2) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x2) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x1) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x1) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
  cncLiftTool()

def cncCutOutsideRectangle(x, y, width, height, toolWidth, cutDepth):
  x1 = x - (toolWidth / 2.0)
  y1 = y - (toolWidth / 2.0)
  x2 = x + width + (toolWidth / 2.0)
  y2 = y + height + (toolWidth / 2.0)
  cncMoveTool(x1, y1)
  cncLowerTool(cutDepth)
  print("G01 X" + cncStr(x2) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x2) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x1) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
  print("G01 X" + cncStr(x1) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
  cncLiftTool()

def cncCutPlane(x, y, width, height, toolWidth, cutDepth):
  x1 = x + (toolWidth / 2.0)
  y1 = y + (toolWidth / 2.0)
  x2 = x + width - (toolWidth / 2.0)
  y2 = y + height - (toolWidth / 2.0)
  cncMoveTool(x1, y1)
  cncLowerTool(cutDepth)
  while True:
    print("G01 X" + cncStr(x2) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
    print("G01 X" + cncStr(x2) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
    print("G01 X" + cncStr(x1) + " Y" + cncStr(y2) + " F" + cncStr(cncVarFeedRate))
    print("G01 X" + cncStr(x1) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
    x1 = x1 + toolWidth / 2.0
    y1 = y1 + toolWidth / 2.0
    x2 = x2 - toolWidth / 2.0
    y2 = y2 - toolWidth / 2.0
    if (x1 > x2) or (y1 > y2):
      break;
    print("G01 X" + cncStr(x1) + " Y" + cncStr(y1) + " F" + cncStr(cncVarFeedRate))
  cncLiftTool()

#cncHeader()

#cncWait(1000)
#cncDrill(10, 0, 1.0)
#cncDrill(20, 0, 1.0)
#cncDrill(30, 0, 1.0)
#cncDrill(40, 0, 1.0)
#for z in [0.2, 0.4, 0.6, 0.8, 1.0]:
#  cncCutInsideRectangle(10, 10, 10, 5, 1.0, z)
#for z in [0.2, 0.4, 0.6, 0.8, 1.0]:
#  cncCutInsideRectangle(15, 10, 11.7, 8.8, 1.0, z)
#cncCutPlane(0, 0, 20, 10, 1.0, 0.5)

#cncMoveTool(0, 5)
#for t in range(0, 20):
#  x1 = 0
#  x2 = 10
#  y = 5 + 0.5 * t
#  print("G01 X" + cncStr(x1) + " Y" + cncStr(y) + " F" + cncStr(cncVarFeedRate))
#  print("G01 Z" + cncStr(-0.04 * t) + " F" + cncStr(cncVarFeedRate))
#  print("G01 X" + cncStr(x2) + " Y" + cncStr(y) + " F" + cncStr(cncVarFeedRate))
#  print("G00 X" + cncStr(x1) + " Y" + cncStr(y) + " F" + cncStr(cncVarMoveRate))

#x = 5
#y = 5
#cncCutPlane(x, y, 8.125, 9.875, 1, 0.4)
#cncCutOutsideRectangle(x-0.375, y-0.375, 8.125 + 0.375*2, 9.875 + 0.375*2, 1, 0.4)

#cncMoveTool(4+-0.5, -0.5)
#for z in [0.5]:
#  cncLowerTool(0.4)
#  cncCutPath(4+12.0+23.0, -0.5)
#  cncCutPath(4+12.0+23.0, 2.0)
#  cncCutPath(4+10.0+23.0, 2.0)
#  cncCutPath(4+10.0+23.0, 7.5)
#  cncCutPath(4+1.5, 7.5)
#  cncCutPath(4+1.5, 2.0)
#  cncCutPath(4-0.5, 2.0)
#  cncCutPath(4-0.5, -0.5)
#cncLiftTool()

#cncMoveTool(4-0.5, -0.5)
#cncLowerTool(0.1)
#cncSetFeedRate(40.0)
#for z in [0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8]:
#  cncSinkTool(z)
#  cncCutPath(4+12.0, -0.5) # +23.0
#  cncCutPath(4+12.0, 2.0)
#  cncCutPath(4+10.0, 2.0)
#  cncCutPath(4+10.0, 7.5)
#  cncCutPath(4+1.5, 7.5)
#  cncCutPath(4+1.5, 2.0)
#  cncCutPath(4-0.5, 2.0)
#  cncCutPath(4-0.5, -0.5)
#cncLiftTool()

#for z in [0.4, 0.8, 1.2]:
#  cncSinkTool(z)
#  print("G02 X0 Y0 I3.5 J0 F5")
#cncLiftTool()

#cncPark()
