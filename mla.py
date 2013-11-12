

def authors(authors):
    """Format authors for a MLA citation.

    >>> authors([])
    ''
    >>> authors(['Vladimir Nabokov'])
    'Nabokov, Vladimir.'
    >>> authors(['Susan Cross', 'Christine Hoffman'])
    'Cross, Susan, and Christine Hoffman.'
    >>> authors(['Theodore Lowi', 'Benjamin Ginsberg', 'Steve Jackson'])
    'Lowi, Theodore, Benjamin Ginsberg, and Steve Jackson.'
    >>> authors(['Sander Gilman', 'Theodore Lowi', 'Benjamin Ginsberg',
    ...              'Steve Jackson'])
    'Gilman, Sander, et al.'
    """
    if len(authors) == 0:
        return ""
    else:
        author = authors[0]
        first, last = author.split()
        if len(authors) == 1:
            return "%s, %s." % (last, first)
        elif len(authors) == 2:
            return "%s, %s, and %s." % (last, first, authors[1])
        elif len(authors) == 3:
            return "%s, %s, %s, and %s." % (last, first, authors[1], authors[2])
        elif len(authors) > 3:
            return "%s, %s, et al." % (last, first)
