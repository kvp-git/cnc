import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 3

g.cncHeader()
g.cncDrill(0,0, 1.0)

for z in [0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.0]:
	#g.cncCutOutsideRectangle(5, 5, 35.7, 65.0, ToolWidth, z)
	g.cncCutOutsideRectangle(5, 5, 21, 34, ToolWidth, z)

g.cncPark()
