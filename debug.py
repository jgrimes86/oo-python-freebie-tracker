import ipdb
from lib import *

#code here

google = Company("Google", 1998)
facebook = Company("Facebook", 2004)
ibm = Company("IBM", 1911)

john = Dev("John")
amy = Dev("Amy")
sam = Dev("Sam")

mug1 = Freebie("yellow mug", 3, john, google)
mug2 = Freebie("blue mug", 3, amy, google)
pen = Freebie("nice pen", 2, john, google)
shirt1 = Freebie("logo t-shirt", 12, amy, facebook)
shirt2 = Freebie("thumbs up t-shirt", 12, sam, facebook)
shirt3 = Freebie("giant face t-shirt", 12, john, facebook)


ipdb.set_trace()