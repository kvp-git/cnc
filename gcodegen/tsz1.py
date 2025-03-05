import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1
TW = ToolWidth / 2

g.cncHeader()
#g.cncDrill(0,0, 0.7)

zList = (0.3, 0.6, 0.9, 1.0)

# side A
#for z in zList:
#	g.cncCutInsideRectangle(10,0, 32.2,31, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(56,0, 32.2,31, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(170-12.2-58,6.4, 12.2,8.4, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(170-7.4-44,0, 7.4,13.4, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(170-12.2-26,6.4, 12.2,8.4, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(170-12.2-8,6.4, 12.2,8.4, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(0,0, 170, 40, ToolWidth, z)

# side B
#for z in zList:
#	g.cncCutInsideRectangle(12,6.4, 9.6,22.2, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(32,6.4, 9.6,22.2, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(52,6.4, 9.6,22.2, ToolWidth, z)
#for z in zList:
#	g.cncCutInsideRectangle(72,6.4, 9.6,22.2, ToolWidth, z)
#for z in zList:
#	g.cncCutOutsideRectangle(0,0, 170, 37, ToolWidth, z)

# side C/D/E
#for z in zList:
#	g.cncCutLine(-1-TW,37+TW, 1+73+TW,40+TW, z)
#for z in zList:
#	g.cncCutOutsideRectangle(0,0, 73, 40, ToolWidth, z)
for z in zList:
	g.cncCutLine(-1-TW,37+TW, 1+73+TW,40+TW, z)
	g.cncCutOutsideRectangle(0,0, 73, 40, ToolWidth, z)

# roof:
#for z in zList:
#	g.cncCutOutsideRectangle(0,0, 172, 75.5, ToolWidth, z)

g.cncPark()
