# similarity.py


def jaccard_similarity(original_text, submitted_text):
    """
    Calculates Jaccard Similarity.
    """

    # Convert to sets
    original_words = set(
        original_text.lower().split()
    )

    submitted_words = set(
        submitted_text.lower().split()
    )

    # Intersection
    common_words = (
        original_words
        .intersection(submitted_words)
    )

    # Union
    total_words = (
        original_words
        .union(submitted_words)
    )

    # Similarity
    similarity_score = (
        len(common_words)
        / len(total_words)
    ) * 100

    return similarity_score, common_words