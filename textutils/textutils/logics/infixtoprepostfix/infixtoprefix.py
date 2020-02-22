def convertInfixString(infix):#all the way its just postfix conversion 
	try:
		stack = []
		poprefix = "";
		operator = ['+','-','*','/','^']
		precedense = {'+':1,'-':1,'*':2,'/':2,'^':3}
		i = 0
		while i < len(infix):
			if infix[i] == ')':
				idx = i
				a=0
				while i < len(infix) and infix[i] != '(':
					i += 1
					if infix[i] == ')': a += 1;
					elif infix[i] == '(' and a>0: a -=1; i += 1;
				poprefix += convertInfixString(infix[idx+1:i]) 	
			
			elif infix[i] in operator:
				if len(stack) == 0:
					stack.append(infix[i]);
				elif precedense[stack[-1]] < precedense[infix[i]]:
					stack.append(infix[i])
				else:
					while len(stack) != 0:
						poprefix += stack.pop();
					stack.append(infix[i])
			else:
				poprefix += infix[i]
				
			i=i+1
		while len(stack) != 0:
			poprefix += stack.pop()
			
		return poprefix
	except Exception as e:
		print(e)

def getInfixString(infix):
	infix = infix[-1::-1]
	infix = convertInfixString(infix)
	return ''.join(infix[-1::-1])
#print(getInfixString("(a-b/c)*(a/k-l)"))
#*-a/bc-/akl