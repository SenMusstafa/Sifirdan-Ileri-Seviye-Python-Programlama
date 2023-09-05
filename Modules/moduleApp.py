import newModule

def module_example():
    # result = help(newModule)
    # result = help(newModule.func)
    result = newModule.number
    result = newModule.numbers
    result = newModule.person["name"]
    result = newModule.person["age"]
    result = newModule.person["city"]
    result = newModule.func(10)

    p = newModule.Person()
    p.speak()
    
    print(result)

if __name__ == "__main__":
    module_example()