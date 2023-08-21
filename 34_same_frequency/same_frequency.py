def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)

    if len(num1) != len(num2):
        return False

    for i in num1:
        if i not in num2:
            return False
        else:
            num2 = num2.replace(i, '', 1)
    return True


