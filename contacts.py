import json
from pathlib import Path
FILE=Path("contacts.json")

def load(): return json.loads(FILE.read_text()) if FILE.exists() else []
def save(x): FILE.write_text(json.dumps(x,indent=2))

contacts=load()
while True:
    print("\n1 Add 2 List 3 Search 4 Delete 5 Exit")
    c=input("> ")
    if c=="1":
        contacts.append({"name":input("Name: "),"phone":input("Phone: "),"email":input("Email: ")})
        save(contacts)
    elif c=="2":
        for x in contacts: print(x)
    elif c=="3":
        q=input("Search: ").lower()
        for x in contacts:
            if q in x["name"].lower() or q in x["phone"]: print(x)
    elif c=="4":
        name=input("Name to delete: ").lower()
        contacts[:]=[x for x in contacts if x["name"].lower()!=name]; save(contacts)
    elif c=="5": break
