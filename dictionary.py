d={"Name":"Rucheel" , "Age":"17" , "Status":"active" , "Profession":"Student"}
print(d)

print(d.get("Name" , "Age"))
d["Status"]="inactive"
print(d)

d.pop("Profession")
print(d)