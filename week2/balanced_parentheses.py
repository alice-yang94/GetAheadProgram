# constants declarations
LEFT_PAREN = '('
RIGHT_PAREN = ')'

def balanced_parentheses(p_str):
    """Find the longest contiguous substring of balanced parentheses

    Args:
        p_str: a string of parentheses

    Returns:
        The length of the longest contiguous substring

    Raises:
        ValueError: An error occurred when input string includes some 
        non-parenthese element
    """
    stack = []
    curr_count = 0
    max_count = 0

    for p in p_str:
        """There are three possible situations:
        - if a single open parenthesis is found: push it to stack
        - if a single close parenthesis is found
            - if the stack is not empty, 
            the pair of parentheses got canceled: 
                pop stack, increment count by 2;
            - else update max count, clear current count;
        """
        if p == LEFT_PAREN:
            stack.append(p)
        elif p == RIGHT_PAREN:
            if len(stack) > 0:
                stack.pop()
                curr_count += 2
            else:
                if curr_count > max_count:
                    max_count = curr_count
                curr_count = 0
        else:
            raise ValueError('Error. Incorrect input!')
    
    if curr_count > max_count:
        return curr_count
    return max_count

