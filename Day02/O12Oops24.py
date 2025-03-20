
class MyStr(str):

    def AppendMr(self):
        return "Mr." + self

st = MyStr("Sachin")
print(st.AppendMr())

print("-" * 60)

class MyListClass(list):

    def Append(self, object):
        print("Record : ", object)
        super().append(object)

l1 = MyListClass()
print(f"l1 :{l1}")
print(type(l1))

l1.Append("Sachin")
l1.Append("Sourav")
l1.Append("Sehwag")

print(f"L1 :{l1}")
