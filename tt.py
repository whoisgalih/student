# Binary encoding
data["school"] = data["school"].replace({"GP": 0, "MS": 1})

data["sex"] = data["sex"].replace({"F": 0, "M": 1})

data["address"] = data["address"].replace({"U": 0, "R": 1})

data["famsize"] = data["famsize"].replace({"LE3": 0, "GT3": 1})

data["Pstatus"] = data["Pstatus"].replace({"T": 0, "A": 1})

data["schoolsup"] = data["schoolsup"].replace({"no": 0, "yes": 1})

data["famsup"] = data["famsup"].replace({"no": 0, "yes": 1})

data["paid"] = data["paid"].replace({"no": 0, "yes": 1})

data["activities"] = data["activities"].replace({"no": 0, "yes": 1})

data["nursery"] = data["nursery"].replace({"no": 0, "yes": 1})

data["higher"] = data["higher"].replace({"no": 0, "yes": 1})

data["internet"] = data["internet"].replace({"no": 0, "yes": 1})

data["romantic"] = data["romantic"].replace({"no": 0, "yes": 1})
