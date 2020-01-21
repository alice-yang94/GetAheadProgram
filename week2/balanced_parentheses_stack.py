# constants declarations
OPEN_PAREN = '('
CLOSE_PAREN = ')'

def balanced_parentheses(p_str):
    """Find the longest contiguous substring of balanced parentheses 
    using stack

    Args:
        p_str: a string of parentheses

    Returns:
        The length of the longest contiguous substring

    Raises:
        ValueError: An error occurred when input string includes some 
        non-parenthese element
    """
    # initial base index is -1
    stack = [-1]
    max_count = 0

    for i,p in enumerate(p_str):
        if p == OPEN_PAREN:
            stack.append(i)
        elif p == CLOSE_PAREN:
            stack.pop()
            if len(stack) > 0:
                # close paren has open paren to match
                # update max_count
                curr_len = i - stack[-1]
                max_count = max(curr_len, max_count)
            else:
                # the curr close paren can not be paired
                # reset base index to current index
                stack.append(i)
        else:
            raise ValueError('Error. Incorrect input!')
    return max_count