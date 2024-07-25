
import camelcase
#here eman is the variable name
eman="this is my trial to try the package"
print(eman)
#here a is the name of object
#the pranthesis identifies as a funtion.
#we need to create venv or install pip for every folder or project we create.
a= camelcase.CamelCase()
print(a.hump(eman))