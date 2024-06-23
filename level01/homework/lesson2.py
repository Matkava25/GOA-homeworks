name = "levan"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "levan" არის ცვლადისთვის მნიშვნელობა

surname = "matkava"

#print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "levan" #ეს არის str (string) ტიპის ცვლადი
age = 25 # ეს არის int (integer) მთელი რიცხვი
height = 187 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming = True #True ან False
is_ugly = False #snakecase(უბრალოდ წერის სტილი სტანდარტულად)

isUgly = False #ჯავასკრიპტული camelcase


print(name + "" + surname)

# #სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
# print(name+age)

print (type(age))
print (type(name))
print (type(surname))
print (type(height))
print (type(knows_programming))

print(name+" " +str(age))