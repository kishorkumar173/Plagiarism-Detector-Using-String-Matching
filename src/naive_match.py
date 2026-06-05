# naive_match.py


def naive_string_match(original_sentences, submitted_sentences):
    """
    Finds exact matching sentences
    using naive string matching.
    """

    matched_sentences = []

    # Compare each sentence
    for sentence in original_sentences:

        cleaned_sentence = sentence.strip().lower()

        for submitted in submitted_sentences:

            cleaned_submitted = submitted.strip().lower()

            # Exact match found
            if cleaned_sentence == cleaned_submitted:
                matched_sentences.append(sentence)

    return matched_sentences