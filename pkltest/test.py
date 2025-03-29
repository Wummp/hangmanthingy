import  pickle

l = ["lise", "hilfe", "martha"]

l.append(input("Eingabe: "))

with open("testpkl.pkl", "wb") as f:
    pickle.dump(l, f)


with open("testpkl.pkl", "rb") as f:
    p = pickle.load(f)

print(type(p))

print(p)