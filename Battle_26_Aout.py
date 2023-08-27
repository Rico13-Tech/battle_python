Adres=input("Tanpri antre adrès IP ou a : ")
Ads=Adres.split(".")
Total_Ad=sum(int(Ad) for Ad in Ads)
premye_lèt=int(Ads[0])
Pot=Total_Ad*premye_lèt
print(Pot)
print(Total_Ad)