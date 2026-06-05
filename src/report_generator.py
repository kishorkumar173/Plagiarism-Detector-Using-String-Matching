# report_generator.py


def generate_report(
        naive_score,
        kmp_score,
        rabin_score,
        jaccard_score,
        final_score,
        matched_sentences,
        common_words
):
    """
    Generates plagiarism report
    and saves it into reports folder.
    """

    report_path = (
        "reports/plagiarism_report.txt"
    )

    with open(
            report_path,
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            "========== "
            "PLAGIARISM REPORT "
            "==========\n\n"
        )

        file.write(
            f"Naive Matching Score: "
            f"{naive_score:.2f}%\n"
        )

        file.write(
            f"KMP Matching Score: "
            f"{kmp_score:.2f}%\n"
        )

        file.write(
            f"Rabin-Karp Score: "
            f"{rabin_score:.2f}%\n"
        )

        file.write(
            f"Jaccard Similarity Score: "
            f"{jaccard_score:.2f}%\n"
        )

        file.write("\n")

        file.write(
            f"Final Plagiarism "
            f"Percentage: "
            f"{final_score:.2f}%\n"
        )

        file.write("\n")

        file.write(
            "========== "
            "MATCHED SENTENCES "
            "==========\n"
        )

        for i, sentence in enumerate(
                matched_sentences, 1):
            file.write(
                f"{i}. {sentence}\n"
            )

        file.write("\n")

        file.write(
            "========== "
            "COMMON WORDS "
            "==========\n"
        )

        file.write(
            ", ".join(common_words)
        )

    return report_path