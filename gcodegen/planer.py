import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1

TH = ToolWidth / 2

g.cncSetToolLiftHeight(1)
g.cncSetFeedRate(1)
g.cncHeader()

z = 0.1

#g.cncCutLines([(10, 0), (10, 10), (0, 10), (0, 0)], z)

g.cncCutPlane(0, 0, 20, 20, ToolWidth, z)

g.cncPark()

