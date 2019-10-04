class chr_data():
    def __init__(self):
        self.name=""
        self.helth=0.0
        self.dps=0.0
        self.Armor=0.0
        self.kaifuku=0.0


#v={"tank":{"c1":{"helth":600,"dps":30},"c2":{"helth":500,"dps":20}},"damege":{"c3":{"helth":200,"dps":80}}}
#print(v)
#print(v["tank"])
#t=v["tank"]
#print(t.values())
#k=t["c1"]
#t=k.values()
list_helth={"D.va":200,"WINSTON":400}
list_dps={"D.va":200,"WINSTON":400}
list_Armor={"D.va":200,"WINSTON":400}
list_kaifuku={"D.va":200,"WINSTON":400}
def nyuryoku():
    tankx=chr_data()
    tankx.name=input("D.vaを入力してください:")
    tankx.helth=list_helth[tankx.name]
    tankx.dps=list_dps[tankx.name]
    if tankx.name in list_Armor.keys():
        tankx.Armor=list_Armor[tankx.name]

    if tankx.name in list_kaifuku.keys():
        tankx.kaifuku=list_kaifuku[tankx.name]
    return tankx.name,tankx.helth,tankx.dps,tankx.Armor,tankx.kaifuku
tankA=nyuryoku()

#tankB=nyuryoku()
print(tankA)
