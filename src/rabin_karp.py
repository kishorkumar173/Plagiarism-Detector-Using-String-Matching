# rabin_karp.py


def rabin_karp_search(text, pattern):
    """
    Rabin-Karp pattern matching algorithm.
    Returns True if pattern found.
    """

    d = 256
    q = 101

    m = len(pattern)
    n = len(text)

    if m > n:
        return False

    pattern_hash = 0
    text_hash = 0
    h = 1

    # Calculate h
    for _ in range(m - 1):
        h = (h * d) % q

    # Initial hash values
    for i in range(m):
        pattern_hash = (
            d * pattern_hash + ord(pattern[i])
        ) % q

        text_hash = (
            d * text_hash + ord(text[i])
        ) % q

    # Sliding window
    for i in range(n - m + 1):

        # Hash match
        if pattern_hash == text_hash:

            # Verify characters
            if text[i:i + m] == pattern:
                return True

        # Calculate next hash
        if i < n - m:

            text_hash = (
                d * (
                    text_hash
                    - ord(text[i]) * h
                )
                + ord(text[i + m])
            ) % q

            if text_hash < 0:
                text_hash += q

    return False


def rabin_document_match(
        original_sentences,
        submitted_sentences
):
    """
    Compare documents using Rabin-Karp.
    """

    matched_sentences = []

    for sentence in original_sentences:

        pattern = sentence.lower().strip()

        for submitted in submitted_sentences:

            text = submitted.lower().strip()

            if rabin_karp_search(text, pattern):
                matched_sentences.append(sentence)
                break

    return matched_sentences