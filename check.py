v={"tank":{"c1":{"helth":600,"dps":30},"c2":{"helth":500,"dps":20}},"damege":{"c3":{"helth":200,"dps":80}}}
#print(v)
#print(v["tank"])
t=v["tank"]
print(t.values())
k=t["c1"]
t=k.values()
for i in t:
    print(i)
