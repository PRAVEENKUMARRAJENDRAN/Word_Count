class WordCount:
    """
    Number of Words in the sentences will be counted.
    
    :param sentences: Senetences to get the words count.
    :type sentences: string

    :return: Number of Words.
    :rtpe: int

    """

    def counter(sentences):
        count = 1
        if sentences == " " or sentences == "":
            return 0
        else:
            for c in sentences:
                if c == " ":
                    count += 1
        return count

