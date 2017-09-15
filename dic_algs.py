ivan = {"name" : "ivan","age":34,"children":[{"name" : "vasja","age":16}] }
sasha = {"name" : "sasha","age":50,"children":[{"name" : "ivan","age":20}, {"name" : "dima","age":22}] }
michael = {"name" : "michael","age":60,"children":[{"name" : "vasja","age":31}] }
emp = [ivan,sasha,michael]
def n(emp):
    mas_emps=[]
    for emp_el in emp:
        for i in emp_el["children"]:
            if i["age"] > 18:
               mas_emps.append(emp_el["name"])
               break
    return mas_emps
print (*n(emp))