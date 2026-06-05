from src.file_handler import read_document
from src.preprocessing import (
    clean_text,
    sentence_tokenization
)

from src.naive_match import naive_string_match
from src.kmp_match import kmp_document_match
from src.rabin_karp import rabin_document_match
from src.similarity import jaccard_similarity
from src.report_generator import (
    generate_report
)


def main():

    # File paths
    original_path = (
        "documents/original.txt"
    )

    submitted_path = (
        "documents/submitted.txt"
    )

    # Read documents
    original_text = read_document(
        original_path
    )

    submitted_text = read_document(
        submitted_path
    )

    # Clean text
    cleaned_original = clean_text(
        original_text
    )

    cleaned_submitted = clean_text(
        submitted_text
    )

    # Tokenization
    original_sentences = (
        sentence_tokenization(
            original_text
        )
    )

    submitted_sentences = (
        sentence_tokenization(
            submitted_text
        )
    )

    # ------------------
    # Naive Matching
    # ------------------
    naive_matches = (
        naive_string_match(
            original_sentences,
            submitted_sentences
        )
    )

    naive_score = (
        len(naive_matches)
        / len(original_sentences)
    ) * 100

    # ------------------
    # KMP Matching
    # ------------------
    kmp_matches = (
        kmp_document_match(
            original_sentences,
            submitted_sentences
        )
    )

    kmp_score = (
        len(kmp_matches)
        / len(original_sentences)
    ) * 100

    # ------------------
    # Rabin-Karp
    # ------------------
    rabin_matches = (
        rabin_document_match(
            original_sentences,
            submitted_sentences
        )
    )

    rabin_score = (
        len(rabin_matches)
        / len(original_sentences)
    ) * 100

    # ------------------
    # Jaccard Similarity
    # ------------------
    jaccard_score, common_words = (
        jaccard_similarity(
            cleaned_original,
            cleaned_submitted
        )
    )

    # ------------------
    # Final Score
    # ------------------
    final_score = (
        naive_score
        + kmp_score
        + rabin_score
        + jaccard_score
    ) / 4

    # Unique matches
    matched_sentences = list(
        set(
            naive_matches
            + kmp_matches
            + rabin_matches
        )
    )

    # Generate report
    report_path = (
        generate_report(
            naive_score,
            kmp_score,
            rabin_score,
            jaccard_score,
            final_score,
            matched_sentences,
            common_words
        )
    )

    # Output
    print(
        "\n========== "
        "PLAGIARISM REPORT "
        "==========\n"
    )

    print(
        f"Final Plagiarism "
        f"Percentage: "
        f"{final_score:.2f}%"
    )

    print(
        f"\nReport Saved At:\n"
        f"{report_path}"
    )


if __name__ == "__main__":
    main()