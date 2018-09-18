sub_total = float(input("Please enter the sub_total: "))
tip = float(input("Please enter the tip percentage: "))

def total_bill(sub_total, tip):
   total = sub_total + (sub_total * (tip / 100))
   return float("{0:.2f}".format(total))

print (total_bill(sub_total, tip))
