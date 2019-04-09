try:
	l=[1,2,3,4,5]
	a=len(l)
	if a>3:
		raise NameError
	elif a<3:
		raise TypeError

except NameError:
	print("no choice")
except TypeError:
	print("error occured")
finally:
	print("execution completed")		
