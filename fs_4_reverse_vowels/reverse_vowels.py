def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels_indexes = []

    for index, char in enumerate(s):
        if char in "aeiouAEIOU":
            vowels_indexes.append(index)

    results = list(s)

    i, j = 0, len(vowels_indexes) - 1
    while i < j:
        results[vowels_indexes[i]], results[vowels_indexes[j]] = results[vowels_indexes[j]], results[vowels_indexes[i]]
        i += 1
        j -= 1

    return "".join(results)


