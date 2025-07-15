# def findMissingInvoice(invoices):
#     if len(invoices)<1:return -1
#     else:
#         minimum = min(invoices)
#         while True:
#             newMinimum = minimum+1
#             if newMinimum in invoices:
#                 minimum = newMinimum
#             else:return newMinimum

def findMissingInvoice(invoices):
    if len(invoices)<1:return -1
    else:
        minimum = min(invoices)
        while True:
            if minimum not in invoices:
                return minimum
            minimum+=1

print(findMissingInvoice([8,10,3,1,4,2,5]))
print(findMissingInvoice([45,91,90,92,46]))
print(findMissingInvoice([0,1,2,4,5,6,7]))
