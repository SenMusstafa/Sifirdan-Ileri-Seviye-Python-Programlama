# Example 1
def scope_example_1():
    x = 'global x'
    
    def function():
        x = 'local x'
    
    function()
    print(x)

# Example 2
def scope_example_2():
    name = 'Mustafa'
    
    def change_name(new_name):
        nonlocal name
        name = new_name
        print(name)
    
    change_name('Sen')
    print(name)

# Example 3
def scope_example_3():
    name = 'global string'
    
    def greeting():
        name = 'Mustafa'
        
        def hello():
            print('hello ' + name)
        
        hello()
    
    greeting()

# Example 4
def scope_example_4():
    global x
    x = 50
    
    def test():
        global x
        print(f'x: {x}')
        x = 100
        print(f'changed x to {x}')
    
    test()
    print(x)

if __name__ == "__main__":
    scope_example_1()
    scope_example_2()
    scope_example_3()
    scope_example_4()
