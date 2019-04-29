"""A simple program to ask the user for input and to use the data in the output."""

name = input('Please enter your name and press enter: ').title().strip()

#asks for the name and greets the user
def greet(name):
	if not name.isnumeric():
		return f'Hello {name}!'
	else:
		return 'Bye!'


# execute only if run as a script
if __name__ == "__main__":
	print(greet(name))