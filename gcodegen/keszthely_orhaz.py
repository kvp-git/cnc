import gcodegen as g

# sizes are in mm
ToolWidth = 1
SheetDepth = 1

TH = ToolWidth / 2

g.cncHeader()
g.cncDrill(0,0, 0.7)

z = 0.5

#g.cncCutLines([(10, 0), (10, 10), (0, 10), (0, 0)], z)

bx1 = 10
by1 = 0

g.cncCutLines([(bx1 - TH, by1 - TH), (bx1 - TH, by1 + 18 + TH), (bx1 + 22 + TH, by1 + 19 + TH), (bx1 + 22 + TH, by1 - TH),
               (bx1 + 18 - TH, by1 - TH), (bx1 + 18 - TH, by1 - 1 - TH), (bx1 + 4 - TH, by1 - 1 - TH), (bx1 + 4 - TH, by1 - TH), (bx1 - TH, by1 - TH)], z)
g.cncCutLine(bx1 + 1 - TH, by1 - TH, bx1 + 1 - TH, by1 + 19 + TH, z)
g.cncCutLine(bx1 + 22 - 1 + TH, by1 - TH, bx1 + 22 - 1 + TH, by1 + 19 + TH, z)
g.cncCutInsideRectangle(bx1 + 22 - 4 - 9, by1 + 12.5 - 9, 9, 9, ToolWidth, z)

g.cncPark()

