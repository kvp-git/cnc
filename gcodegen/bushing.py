import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 3

g.cncHeader()
#g.cncDrill(0,0, 0.7)

zList = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
#zList = (2.5, 3.0)

#for z in zList:
#	g.cncCutInsideCircle(0,0, 7.7 / 2, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideCircle(0,0, 12.0 / 2, ToolWidth, z)

for z in zList:
	g.cncCutInsideCircle(0,0, 6.0 / 2, ToolWidth, z)
for z in zList:
	g.cncCutOutsideCircle(0,0, 12.0 / 2, ToolWidth, z)

g.cncPark()
