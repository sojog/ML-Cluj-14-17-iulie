
l = ["cer", "cafea", "apa"]
print(l, len(l), l[0])

d = {
    "albastru": "cer",  "negru": "cafea", "transparent":"apa"
}
print(d, len(d), d["albastru"])


d["rosu"] = "sange"
print(d, len(d))


d["rosu"] = "mare"
d["verde"] = "salata"
print(d, len(d))


print(d.keys())
print(d.values())

d.clear()
print(d)