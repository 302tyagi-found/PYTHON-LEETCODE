# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
#
# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.
#
# It is guaranteed that the given expression is valid and follows the given rules.
#
#

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Function to evaluate based on the operator and list of boolean results
        def evaluate(operator, values):
            if operator == '!':
                # NOT has only one subexpression
                return not values[0]
            elif operator == '&':
                # AND: all subexpressions must be True
                return all(values)
            elif operator == '|':
                # OR: at least one subexpression must be True
                return any(values)

        # Stack to keep track of operators and subexpressions
        stack = []

        for char in expression:
            if char == ',':
                # Ignore commas as they are just separators
                continue
            elif char in 'tf':
                # Convert 't' to True and 'f' to False and push to stack
                stack.append(True if char == 't' else False)
            elif char in '!&|':
                # Push the operator to stack
                stack.append(char)
            elif char == '(':
                # Push a marker to identify the start of a subexpression
                stack.append('(')
            elif char == ')':
                # Process the subexpression between '(' and ')'
                values = []
                while stack and stack[-1] != '(':
                    values.append(stack.pop())
                stack.pop()  # Pop the '(' marker
                operator = stack.pop()  # Pop the operator ('!', '&', or '|')
                # Evaluate the subexpression
                result = evaluate(operator, values[::-1])  # Reverse to maintain original order
                stack.append(result)  # Push the result back to the stack

        # Final result will be the last element in the stack
        return stack.pop()