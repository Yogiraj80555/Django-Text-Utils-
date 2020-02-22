#max recursion depth of python in jupyter notebook is 2959 functions of 4 line as date 12/2/2020 on Intel Xeon w-2125 4.00GHZ with 32GB DDR4 64 windows10

#check results for like multi length operand like abc+bcq*ewq+pq etc....
#check this condition a+b*c(w*e/r+e it's an inproper format
#currently working for only () this brackets
def getInfixString(infix):
	try:
		stack = []
		postfix = "";
		operator = ['+','-','*','/','^']
		precedense = {'+':1,'-':1,'*':2,'/':2,'^':3}
		i = 0;
		while i<len(infix):
			if infix[i] == '(':
				idx = i;
				a=0
				while i<len(infix) and infix[i] != ')':
					i +=1;
					if infix[i] == '(': a += 1;
					if infix[i] == ')' and a>0: i+=1; a -=1;
				
				if infix[i] != ')':
					return "Invalid Infix Expression";
				postfix += getInfixString(infix[idx+1:i])
		
			elif infix[i] in operator:
				if len(stack) == 0:
					stack.append(infix[i]);
					i += 1 #here we increment i cause below we use continue, otherwise last line of this while loop will work for as also if we don't use continue
					continue;
				elif precedense[infix[i]] > precedense[stack[-1]]:
					stack.append(infix[i]);
				else:
					while len(stack) != 0:
						postfix += stack.pop();
					stack.append(infix[i])
			else:
				postfix += infix[i];
			i += 1;
		while len(stack) != 0:
			postfix += stack.pop()
		return postfix;
	except Exception as e:
		print(e)
		return "Invalid Infix Expression String";
		
	
