def precedence(operator):
    if operator == "^":
        return 3
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 1
    else:
        return 0

def infix_to_postfix(exp):
    stack=[]
    postfix=""

    for ch in exp:
        if ch.isalnum():
            postfix+=ch

        elif ch == "(":
            stack.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix+=stack.pop()
            stack.pop()

        else:
            while stack and stack[-1] != "(" and precedence(stack[-1]) > precedence(ch):
                postfix+=stack.pop()
            stack.append(ch)

    while stack!=[]:
        postfix+=stack.pop()

    return postfix


def infix_to_prefix(exp):
    exp=exp[::-1]
    exp=exp.replace("(", "#")
    exp=exp.replace(")", "(")
    exp=exp.replace("#", ")")

    postfix=infix_to_postfix(exp)

    return postfix[::-1]


exp=input("Enter infix expression: ")
exp=exp.replace(" ", "")

print("Prefix:", infix_to_prefix(exp))
