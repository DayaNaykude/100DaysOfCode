try:
    file = open("a_data.txt")
    my_dict = {"key": "value"}
    print(my_dict["abc"])
except FileNotFoundError:
    file = open("a_data.txt", "w")
    file.write("Hello World!")
except KeyError as error_message:
    print(f"Key {error_message} was not there")
else:
    print(file.read())
finally:
    file.close()
    print("File was closed!")
