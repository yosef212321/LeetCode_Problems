class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for  x in tokens:
            if x == "+":
                sum = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(sum)
            elif x == "-":
                difference = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(difference)
            elif x == "*":
                product = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(product)

            elif x == "/":
                quotient = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(quotient)
            else:
                stack.append(int(x))
        return int(stack[-1])
