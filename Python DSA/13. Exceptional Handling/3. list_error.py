try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[99]) # Result in IndexError
    print(my_list[0]/ my_list[-1]) # Result in ZeroDivisionError
    print(my_list.remove(5))
    my_list = [i for i in range(10**8)]  # MemoryError: Unable to allocate...
    print(my_list.foo())  # AttributeError: 'list' object has no attribute 'foo'

    
except ZeroDivisionError:
    print(f"Cannot divide by zero.")
except IndexError:
    print("Index out of range")
except ValueError:
    print("You're trying to remove or search for exists in the list")
except AttributeError:
    print("no attribute 'foo'")
except MemoryError:
    print("Unable to allocat memory")
except:
    print("Some error occurred")