import numpy as np
import tools

print("Question 1:")
print(-np.pv(rate=.0200/2, nper=50, pmt=5, fv=100))

print("Question 2:")
print(tools.pvp(rate=.0700/2, pmt=6.25))

print("Question 3:")
print(np.fv(rate=.04/12, nper=120, pv=1000000, pmt=14000))

print("Question 4:")
print(tools.pvp(rate=.0300, pmt=10, growth=.1200))

print("Question 5:")
pmt = 1000
pv = 0
i = 1
while (i <= 30):
  discount = 1 / ( (1 + .0350) ** i )
  if (i == 1):
    pv += pmt * discount
  elif (i <= 5):
    pmt = pmt * 1.1
    pv += pmt * discount
  else:
    pv += pmt * discount
  i += 1
print(pv)

print("Question 6:")
fv_ann = -np.pv(rate=.0300, nper=25, pmt=10000, fv=0)
pv_ann = -np.pv(rate=.0300, nper=20, pmt=0, fv=fv_ann)
print(pv_ann)

print("Question 7:")
print(2*np.rate(nper=40, pmt=30, pv=-893.22, fv=1000))
