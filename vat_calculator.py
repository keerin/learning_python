# to do - Add colour. Limit screen size. Stop instant closing in Windows
# -*- coding: cp1252 -*-

print "This is a VAT calculator."
print "Enter the cost excluding VAT below and hit return."
print "You'll be given the cost including vat."
exvat=raw_input("£")
vat=float(exvat)*.2
total=float(exvat)+(vat)
print "VAT is",(vat)
print "Cost including VAT is",(total)
