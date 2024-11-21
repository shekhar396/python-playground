try:
    value=int(input("Enter number:  "))
    print(1/value)
except ValueError:
    print("I dont proceed")
except ZeroDivisionError:
    print("Zero Division")
except:
    print('Something strange has happened here... Sorry!')
