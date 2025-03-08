# import demo as d
# import quote as q
import my_package.demo as d
import my_package.quote as q

name = input("Enter your name: ")
print(d.printing(name))
print(q.get_quote())