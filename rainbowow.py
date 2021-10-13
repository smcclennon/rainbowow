from termcolor import colored

#print("Greg, say hello to:")
#x = input()
#print("Hello " + x +" :)")
#input()

print("Enter text to be coloured red:")
text = colored(input(), 'red')
print("Coloured text: " + text)
input()

#colours = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan']
#print("Enter text to be coloured:")
#for color in colours
#text = colored(input(), colours)
#print("Coloured text: " + text)
#input()