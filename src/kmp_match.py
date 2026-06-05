# kmp_match.py


def compute_lps(pattern):
    """
    Computes Longest Prefix Suffix (LPS) array.
    """

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    KMP string matching algorithm.
    Returns True if pattern found.
    """

    lps = compute_lps(pattern)

    i = 0  # text index
    j = 0  # pattern index

    while i < len(text):

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            return True

        elif i < len(text) and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False


def kmp_document_match(original_sentences, submitted_sentences):
    """
    Finds matching sentences using KMP.
    """

    matched_sentences = []

    for sentence in original_sentences:

        pattern = sentence.lower().strip()

        for submitted in submitted_sentences:

            text = submitted.lower().strip()

            if kmp_search(text, pattern):
                matched_sentences.append(sentence)
                break

    return matched_sentences