import math
Budget = float(input("Budget:"))
YodaCost = 20
BeyBladeCost = 7.2
StickyHandCost = 0.5
YodaThingies = math.floor(int(Budget / YodaCost))
Budget = Budget % YodaCost
print("Yoda:")
print(YodaThingies)
BeyBlades = math.floor(int(Budget / BeyBladeCost))
Budget = Budget % BeyBladeCost
print("BeyBlades:")
print(BeyBlades)
StickyHands = math.floor(int(Budget / StickyHandCost))
Budget = Budget % StickyHandCost
print("StickyHands:")
print(StickyHands)