#coding: UTF8
"""
wchartype
Retrieves character types of double-byte (full-width) characters.
"""

__license__ = "MIT"
__version__ = "0.1"
__author__ = "Ryan Ginstrom"
__description__ = "Retrieves character types of double-byte characters."

# 0x3000 is ideographic space (i.e. double-byte space)
IDEOGRAPHIC_SPACE = 0x3000

def is_asian(char):
    """Is the character Asian?
    
    >>> is_asian('a')
    False
    >>> is_asian(u'\u65e5')
    True
    >>> is_asian(unichr(0x3000))
    False
    
    """

    return ord(char) > IDEOGRAPHIC_SPACE

def is_full_width(char):
    """
    Is the character full width?
    It will be full width if it's Asian or an ideographic space.
    
    >>> is_full_width('a')
    False
    >>> is_full_width(u'\u65e5')
    True
    >>> is_full_width(unichr(0x3000))
    True
    """
    return is_asian(char) or ord(char) == IDEOGRAPHIC_SPACE

def is_kanji(char):
    """
    Returns whether char is kanji (or Chinese)

    >>> is_kanji(u'\u4E40')
    True
    >>> is_kanji(u"a")
    False
    """

    code = ord(char)
    return 0x4E00 <= code <= 0x9FFF

is_hanzi = is_kanji

def is_hiragana(char):
    """
    Returns whether char is hiragana

    >>> is_hiragana(u'a')
    False
    >>> is_hiragana(u'\u308F') # わ
    True
    >>> is_hiragana(u'\u30EA') # リ
    False
    """

    code = ord(char)
    return 0x3041 <= code <= 0x309F

def is_katakana(char):
    """
    Returns whether char is katakana

    >>> is_katakana(u'$')
    False
    >>> is_katakana(u'\u30EA') # リ
    True
    >>> is_katakana(u'\u308F') # わ
    False
    """

    code = ord(char)
    return 0x30A0 <= code <= 0x30FF

def is_half_katakana(char):
    """
    Returns whether char is half-width katakana

    >>> is_half_katakana(u'$')
    False
    >>> is_half_katakana(u'\uFF91') # ﾑ
    True
    >>> is_half_katakana(u'\u30EA') # リ
    False
    """

    code = ord(char)
    return 0xFF65 <= code <= 0xFF9F

def is_hangul(char):
    """
    Returns whether char is hangul

    >>> is_hangul(u'1')
    False
    
    # halfwidth hangul
    >>> is_hangul(u'\uFFB8') # HALFWIDTH HANGUL LETTER CIEUC 
    True

    # fullwidth hangul
    >>> is_hangul(u'\uB973') # 륳
    True

    >>> is_hangul(u'\u30EA') # リ
    False
    """

    code = ord(char)
    # halfwidth hangul
    if 0xFFA0 <= code <= 0xFFDC:
        return True
    # fullwidth hangul
    return 0xAC00 <= code <= 0xD7A3

def is_full_punct(char):
    """
    Returns whether char is full-width punctuation

    >>> is_full_punct(u'$')
    False
    >>> is_full_punct(u'\uFF05') # ％
    True
    >>> is_full_punct(u'\uFF1E') # ＞
    True
    >>> is_full_punct(u'\uFF3D') # ］
    True
    >>> is_full_punct(u'\uFF5B') # ｛
    True
    >>> is_full_punct(u'\u30EA') # リ
    False
    """

    code = ord(char)
    return any(x <= code <= y
               for x, y in [(0xFF01, 0xFF0F),
                        (0xFF1A, 0xFF20),
                        (0xFF3B, 0xFF40),
                        (0xFF5B, 0xFF64)])

def is_full_digit(char):
    """
    Returns whether char is full-width digit

    >>> is_full_digit(u'1')
    False
    >>> is_full_digit(u'\uFF15') # ５
    True
    >>> is_full_digit(u'\uFF05') # ％
    False
    """

    code = ord(char)
    return 0xFF10 <= code <= 0xFF19

def is_full_letter(char):
    """
    Returns whether char is full-width letter.
    This differs from the built-in isalpha method for strings,
    because isalpha will return True for CJK characters.

    >>> is_full_letter(u'\u308F') # hiragana wa (わ)
    False
    >>> u'\u308F'.isalpha() # hiragana wa (わ)
    True

    >>> is_full_letter(u'A')
    False
    >>> is_full_letter(u'\uFF31') # Ｑ
    True
    >>> is_full_letter(u'\uFF4A') # ｊ
    True
    >>> is_full_letter(u'\u30EA') # リ
    False
    >>> is_full_letter(u'\uFF15') # ５
    False
    """

    code = ord(char)
    if 0xFF21 <= code <= 0xFF3A:
        return True
    if 0xFF41 <= code <= 0xFF5A:
        return True
    
    return False

def _test():
    """Run doc tests"""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
