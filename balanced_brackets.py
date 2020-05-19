open_brackets = ["[","{","("] 
close_brackets = ["]","}",")"] 
bracket_pairs =  {"]":"[", "}":"{", ")":"("}
def isBalanced(str):
    stack = [] 
    for i in str:
      if i in open_brackets or i in close_brackets:
        if i in open_brackets: 
            stack.append(i)
        elif i in close_brackets: 
            if (len(stack) > 0): 
                top_element = stack.pop()
                if top_element != bracket_pairs[I]:
                    return "Unbalanced String."
            else: 
                return "Unbalanced String"
    if len(stack) == 0: 
        return "Balanced String"
    else: 
        return "Unbalanced String"

# Main
mystring1 = "{[]{()}}"
mystring2 = "{123(456[.768])}"
mystring3 = "(1+3)-(2-3))"
print(f"{mystring1} is {isBalanced(mystring1)}") 
print(f"{mystring2} is {isBalanced(mystring2)}") 
print(f"{mystring3} is {isBalanced(mystring3)}") 
