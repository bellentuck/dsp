# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

#%%

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """    
    
    if type(count) != int:
        raise Exception('This function requires an integer as input.')
    
    if 0 <= count < 10:
        return 'Number of donuts: ' + str(count)    
    else:
        return 'Number of donuts: many'
    
    #raise NotImplementedError

#%%

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
   
    if type(s) != str:
        raise Exception('This function requires a string as input.')
        
    elif len(s) >= 2:
        s = s[0:2] + s[-2:]  
        return s
    else:
        return ''     
    
    #raise NotImplementedError

#%%

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    
    s = list(s) 
    return s[0] + ''.join([char.replace(char, '*') if char == s[0] \
                  else char for char in s[1:]])
    
    #raise NotImplementedError

#%%

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """

    new_a = a.replace(a[0:2], b[0:2]) 
    new_b = b.replace(b[0:2], a[0:2])
    return new_a + ' ' + new_b 
   
    #raise NotImplementedError

#%%

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swimming')
    'swimmingly'
    >>> verbing('do')
    'do'
    """
    
    if type(s) != str:
        raise Exception('This function requires a string as input.')    
    
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s + 'ing'        
    
    #raise NotImplementedError

#%%

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    not_string = s.find('not')
    bad_string = s.find('bad') + 3

    if not_string != -1 and bad_string > not_string:
        s = s.replace(s[not_string:bad_string], 'good')
        return s
    else:
        return s
    
    #raise NotImplementedError

#%%

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """

    split = lambda x: len(x)/2 + 1      
    
    if type(a) != str or type(b) != str:
        raise Exception('This function requires two strings as input.')
        
    if len(a) % 2 == 0:
        a_front = a[:len(a)/2]
        a_back = a[len(a)/2:]
    else:
        a_front = a[:split(a)]
        a_back = a[split(a):]

    if len(b) % 2 == 0:
        b_front = b[:len(b)/2]
        b_back = b[len(b)/2:]
    else:
        b_front = b[:split(b)]
        b_back = b[split(b):]

    return a_front + b_front + a_back + b_back
    
    #raise NotImplementedError
