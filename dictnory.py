# dic={"name":"ankit",
#       "learnig":"code",
#       "age":34,
#       "is_adult":True,
#       "marke":34.5,
# }

# print(dic["age"])
# dic["name"]="pooja"
# dic["surname"]="singh"
# print(dic)
dic={
    "name":"ankit Singh",
    "Subject":{#nestered Dictionry
        "Math":99,
        "chimistry":66,
        "hindi":67
    }
}
print(dic)
print(dic["Subject"]["hindi"])
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("name"))
print(len(dic))
dic.update({"city":"delhi"})
print(dic)
