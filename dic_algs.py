ivan = {"name" : "ivan","age":34,"children":[{"name" : "vasja","age":16}] }
shashya = {"name" : "shashya","age":50,"children":[{"name" : "ivan","age":20}] }
michael = {"name" : "michael","age":60,"children":[{"name" : "vasja","age":31}] }
emp = [ivan,shashya,michael]
for x in emp:
    for i in x["children"]:
        if i["age"] >18:
            print(x["name"])

