import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1

WallW = 30 - SheetDepth
WallH = 24

B0X = 5
B1X = B0X + WallW + ToolWidth
B2X = B1X + WallW + ToolWidth
B3X = B2X + WallW + ToolWidth

g.cncHeader()
g.cncDrill(0,0, 0.7)

#g.cncCutPlane(B0X - ToolWidth, 0, WallW * 4 + ToolWidth * 5, 3, ToolWidth, 0.3)

# ajto 1
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B0X+5,3, 6,15, ToolWidth, z)

# ablak 1
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B0X+30-4-7.8,3+15-11.8, 7.8,11.8, ToolWidth, z)

# ablak 2
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B2X+4,3+15-11.8, 7.8,11.8, ToolWidth, z)

# ajto 2
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B1X+(30-7)/2,3, 7,15, ToolWidth, z)

# kis ablakok
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B3X+8-3.1/2,15+3-4.7, 3.1,4.7, ToolWidth, z)
for z in (0.5, 1.0):
	g.cncCutInsideRectangle(B3X+30-8-3.1/2,15+3-4.7, 3.1,4.7, ToolWidth, z)

g.cncCutOutsideRectangle(B0X, 0, WallW, WallH, ToolWidth, 0.7)
g.cncCutOutsideRectangle(B1X, 0, WallW, WallH, ToolWidth, 0.7)
g.cncCutOutsideRectangle(B2X, 0, WallW, WallH, ToolWidth, 0.7)
g.cncCutOutsideRectangle(B3X, 0, WallW, WallH, ToolWidth, 0.7)

"""
# ajto 2
for z in (0.2, 0.4, 0.6, 0.8, 1.0):
	g.cncCutInsideRectangle((4+1), (1+6), 2,2, ToolWidth, z);
	g.cncCutInsideRectangle((4+4), (1+6), 2,2, ToolWidth, z);
	g.cncCutInsideRectangle((4+1), (1+9), 2,2, ToolWidth, z);
	g.cncCutInsideRectangle((4+4), (1+9), 2,2, ToolWidth, z);
	g.cncCutInsideRectangle((4+1), (1+12), 2,2, ToolWidth, z);
	g.cncCutInsideRectangle((4+4), (1+12), 2,2, ToolWidth, z);
g.cncCutInsideRectangle((4+1), (1+1), 5,4, ToolWidth, 0.2);
g.cncCutInsideRectangle((4+2), (1+2), 3,2, ToolWidth, 0.2);
g.cncCutOutsideRectangle(4,1, 7,15, ToolWidth, 0.3);
g.cncCutOutsideRectangle(3,0, 9,17, ToolWidth, 0.4);
g.cncCutOutsideRectangle(3,0, 9,17, ToolWidth, 0.9);
#g.cncCutOutsideRectangle(3,0, 9,17, ToolWidth, 1.1);
"""
"""
# teto
g.cncCutOutsideRectangle(3,3, 38,38, ToolWidth, 0.3);
g.cncCutOutsideRectangle(2,2, 40,40, ToolWidth, 0.5);
g.cncCutOutsideRectangle(2,2, 40,40, ToolWidth, 1.0);
"""
g.cncPark()
