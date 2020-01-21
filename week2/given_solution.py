'''provided by get ahead program ANZ 2020'''

def longest_balanced(string):
    # Seed the stack with a "base" index of -1. The base holds the index
    # immediately before the current run of balanced parentheses.
    stack = [-1]  # O(n) space.
    longest = 0
    for i, char in enumerate(string):
        if char == '(':
            # Remember the index of the opening parenthesis.
            stack.append(i)
        elif char == ')':
            # A closing parenthesis either matches and discards the last opening one,
            # or is unmatched and discards the base index.
            stack.pop()
            if stack:
                # Compute the current length against the last open parenthesis or the
                # base (which occurs when the current chain is fully balanced), and
                # track the maximum of these.
                longest = max(longest, i - stack[-1])
            else:
                # This is the unmatched case, which means the current chain of balanced
                # parentheses has been broken. Reset the base index to our current index
                # to start tracking a new chain, starting from the next character.
                stack.append(i)
    # Return the maximum.
    return longest

# You don't necessarily have to write test code in an interview, but
# you are still expected to provide meaningful test cases and try some
# manually.
if __name__ == '__main__':
    assert longest_balanced('') == 0
    assert longest_balanced('(') == 0
    assert longest_balanced(')') == 0
    assert longest_balanced('()(') == 2
    assert longest_balanced('())') == 2
    assert longest_balanced('(())') == 4
    assert longest_balanced('()()') == 4
    assert longest_balanced('(()())') == 6
    assert longest_balanced('())(())') == 4
    assert longest_balanced(')(()))))(((()') == 4
    assert longest_balanced('(()())((((()))))') == 16