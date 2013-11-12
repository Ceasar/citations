



class JournalArticle(object):
    pass


class Book(object):
    """
    """
    def __init__(self,
                 authors,
                 title_of_book,
                 place_of_publication,
                 publisher,
                 date_of_publication,
                 medium_of_publication,
                 ):
        self.authors = authors
        self.title_of_book = title_of_book
        self.place_of_publication = place_of_publication
        self.publisher = publisher
        self.date_of_publication = date_of_publication
        self.medium_of_publication = medium_of_publication

    @property
    def mla_citation(self):
        """
        >>> b0 = Book(["Vladmir Nabokob"], "Lolita", "New York", "Putnam",
        ...          1955, "Print")
        >>> b0.mla_citation
        "Nabokov, Vladimir. Lolita. New York: Putnam, 1955. Print."

        Two authors:

        >>> b1 = Book(["Susan Cross", "Christine Hoffman"], "Bruce Nauman: Theaters of Experience", "New York", "Guggenheim Musuem",
        ...          1955, "Print")
        >>> b1.mla_citation
        "Cross, Susan, and Christine Hoffman. Bruce Nauman: Theaters of Experience. New York: Guggenheim Museum; London: Thames & Hudson, 2004. Print."

        No author:

        >>> b2.mla_citation
        "Peterson's Annual Guides to Graduate Study. 33rd ed. Princeton, NJ: Peterson's, 1999. Print."

        """
        authors = "%s, %s." 
        return authors + "%s. %s: %s, %s. %s." % ()
