def reverse(string):
    """Reverse string

    >>> reverse('')
    ''

    >>> reverse('Hexlet')
    'telxeH'
    """


    return string[::-1]


# Нужно для запуска тестов
# 1) python3 -i example.py
# 2) >>> reverse('')
# ''
# >>> reverse('Hexlet')
# 'telxeH'
#if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
# 3) python3 example.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()
