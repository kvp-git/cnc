import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1

g.cncHeader()
#g.cncDrill(0,0, 0.7)

zList = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0)

for z in zList:
	g.cncCutOutsideRectangle(0,0, 90, 78, ToolWidth, z)

g.cncPark()
