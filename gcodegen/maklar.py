import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1

g.cncHeader()
#g.cncDrill(0,0, 0.7)

zList = (0.3, 0.6, 1.0)

#XB = 1
#YB = 1
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+37, 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+(37+8+38), 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(XB,YB, 25,128, ToolWidth, z)

#XB = 25
#YB = 1
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+37, 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+(37+8+38), 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(XB+10,YB, 15,128, ToolWidth, z)

#XB = 1
#YB = 1
#for z in zList:
#	g.cncCutInsideRectangle(XB+3,YB+12, 12,6, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+35, 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+(35+8+8+6+8), 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+(10+5),YB+(35+8+8), 5,6, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+(10+5),YB+(35+8+8+6+8+8+38), 5,6, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(XB,YB, 25,128, ToolWidth, z)

#XB = 25
#YB = 1
#for z in zList:
#	g.cncCutInsideRectangle(XB+3,YB+12, 12,6, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+35, 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+10,YB+(35+8+8+6+8), 10,8, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+(10+5),YB+(35+8+8), 5,6, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(XB+(10+5),YB+(35+8+8+6+8+8+38), 5,6, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(XB+10,YB, 15,128, ToolWidth, z)

TW = ToolWidth / 2

for z in zList:
	g.cncCutLine(-TW,-TW, 42+TW,-TW, z)
	g.cncCutLine(42+TW,-TW, 42+TW,15+TW, z)
	g.cncCutLine(42+TW,15+TW, 42-8.75, 8.75+15, z)
	g.cncCutLine(42-8.75,15+8.75, 21,40+TW, z)
	g.cncCutLine(21,40+TW, 8.75,15+8.75, z)
	g.cncCutLine(8.75,15+8.75, 0-TW,15+TW, z)
	g.cncCutLine(0-TW,15+TW, -TW,-TW, z)

g.cncPark()
