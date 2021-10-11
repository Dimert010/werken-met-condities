kaas = input('is de kaas geel? (y/n)')

if kaas == "n":
    schimmel = input('heeft de kaas blauwe schimmels? (y/n)')
    if schimmel == "y":
        korst = input("heeft de kaas een korst? (y/n)")
        if korst == "y":
            print("Bleu de rochbaron")
        if korst == "n":
            print("fourme dambert")
    if schimmel == "n":
        korst = input("heeft de kaas een korst")
        if korst == "y":
            print("cambembert")
        if korst == "n":
            print("mozzarella")
if kaas == "y":
   gaten = input('zitten er gaten in? (y/n)')
   if gaten == "n":
       steen = input('is de kaas hard van steen? (y/n)')
       if steen == "y":
           print("parmigiano reggiano")
       if steen == "n":
           print("goudse kaas")
   if gaten == "y":
       duur=input('is de kaas belachelijk duur? (y/n)')
       if duur == "n":
           print("leerdammer")
       if duur == "y":
           print("emmenthaler")
           




    


    





