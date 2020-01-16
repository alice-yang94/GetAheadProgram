# constants declarations
OPEN_PAREN = '('
CLOSE_PAREN = ')'

def balanced_parentheses(p_str):
    """Find the longest contiguous substring of balanced parentheses 
    using counter

    Args:
        p_str: a string of parentheses

    Returns:
        The length of the longest contiguous substring

    Raises:
        ValueError: An error occurred when input string includes some 
        non-parenthese element
    """
    open_paren_count = 0
    curr_len_count = 0
    max_len_count = 0

    for p in p_str:
        """There are three possible situations:
        - if a single open parenthesis is found: 
        increment OPEN_PAREN count
        - if a single close parenthesis is found
            - if OPEN_PAREN left to to be paired,  
            the pair of parentheses got canceled: 
            decrement OPEN_PAREN count, increment length count by 2;
            - else update max len count, clear current len count;
        """
        if p == OPEN_PAREN:
            open_paren_count += 1
        elif p == CLOSE_PAREN:
            if open_paren_count > 0:
                open_paren_count -= 1
                curr_len_count += 2
            else:
                if curr_len_count > max_len_count:
                    max_len_count = curr_len_count
                curr_len_count = 0
        else:
            raise ValueError('Error. Incorrect input!')
    
    if curr_len_count > max_len_count:
        return curr_len_count
    return max_len_count

