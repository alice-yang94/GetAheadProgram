def get_largest_area(inputArray):
    """
    Returns the indices of given array that represent the largest area 
    under the curve formed by a given array of non-negative integers 
    that represented by bars (y value) in a histogram 
    (with the array index being the x value) and above the axis. 

    Args:
        inputArray: a given array of non-negative integers
    """
    # store the indices of inputArray in the stack
    # the corresponding values of the indices in the stack are increasing
    # from bottom to top
    stack = []
    # keep record of the current max. area and corresponding indices
    maxArea = 0
    maxIndices = None

    # calculate the largest area start from each index in the inputArray
    currIdx = 0
    while currIdx < len(inputArray):
        if not stack:
            # if stack is empty, move the pointer to the next value in
            # the inputArray
            stack.append(currIdx)
            currIdx += 1
        else:
            prevIdx = stack[-1]
            prevValue = inputArray[prevIdx]
            currValue = inputArray[currIdx]
            
            if currValue >= prevValue:
                # if current value is not smaller than previous value,
                # move the pointer to next value
                stack.append(currIdx)
                currIdx += 1
            else:
                # if the current value is smaller than the previous value 
                # in the stack, calculate the largest area formed from 
                # (the second index in the stack + 1) to 
                # (the current index - 1), 
                # with the height as the corresponding value of the 
                # top index in the stack.
                # update max area and indices if needed
                stack.pop()
                beginIdx = stack[-1] if stack else -1
                currArea = (currIdx - beginIdx - 1) * prevValue
                if currArea > maxArea:
                    maxArea = currArea
                    maxIndices = (beginIdx+1, currIdx-1)

    # pop all elements from the stack and update max area and indices
    lastIdx = len(inputArray) - 1
    while stack:
        currIdx = stack.pop()
        currValue = inputArray[currIdx]
        beginIdx = stack[-1] if stack else -1
        currArea = (lastIdx - beginIdx) * currValue
        if currArea > maxArea:
            maxArea = currArea
            maxIndices = (beginIdx+1, lastIdx)
        
    return maxArea, maxIndices