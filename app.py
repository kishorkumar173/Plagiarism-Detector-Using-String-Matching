
import streamlit as st

from src.preprocessing import (
    clean_text,
    sentence_tokenization
)

from src.naive_match import naive_string_match
from src.kmp_match import kmp_document_match
from src.rabin_karp import rabin_document_match
from src.similarity import jaccard_similarity


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Plagiarism Detector",
    page_icon="📄",
    layout="wide"
)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("📘 Project Information")

st.sidebar.markdown("""
### Algorithms Used
- Naive String Matching
- KMP Algorithm
- Rabin–Karp Algorithm
- Jaccard Similarity

### Features
✅ Exact Match Detection  
✅ Near Duplicate Detection  
✅ Similarity Score  
✅ Matched Sentence Extraction  

### Tech Stack
- Python
- Streamlit
- NLTK
- DSA Algorithms
""")

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #071124 0%,
        #0B1426 50%,
        #111827 100%
    );
    color: white;
}

/* Hide Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Title */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: white;
}

.subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Upload Card */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(6,182,212,0.3);
}

/* Upload Text */
[data-testid="stFileUploader"] label {
    color: white !important;
    font-size: 17px !important;
    font-weight: bold !important;
}

[data-testid="stFileUploader"] p {
    color: #E2E8F0 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(
        135deg,
        #2563EB,
        #06B6D4
    );
    color: white;
    font-size: 18px;
    font-weight: bold;
}

/* Metrics */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Final Score Card */
.final-card {
    background: linear-gradient(
        135deg,
        #06B6D4,
        #2563EB
    );
    border-radius: 28px;
    padding: 35px;
    text-align: center;
    color: white;
    margin-top: 20px;
}

/* Match Box */
.match-box {
    background: rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    border-left: 4px solid #06B6D4;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.markdown(
    '<div class="main-title">'
    '📄 Plagiarism Detector'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Using KMP, Rabin-Karp & Similarity Algorithms'
    '</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    original_file = st.file_uploader(
        "📂 Upload Original Document",
        type=["txt"]
    )

with col2:
    submitted_file = st.file_uploader(
        "📂 Upload Submitted Document",
        type=["txt"]
    )

# ------------------------------------------------
# BUTTON
# ------------------------------------------------
if st.button("🚀 Check Plagiarism"):

    if original_file and submitted_file:

        # Read files
        original_text = (
            original_file.read()
            .decode("utf-8")
        )

        submitted_text = (
            submitted_file.read()
            .decode("utf-8")
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

        # Naive
        naive_matches = naive_string_match(
            original_sentences,
            submitted_sentences
        )

        naive_score = (
            len(naive_matches)
            / len(original_sentences)
        ) * 100

        # KMP
        kmp_matches = kmp_document_match(
            original_sentences,
            submitted_sentences
        )

        kmp_score = (
            len(kmp_matches)
            / len(original_sentences)
        ) * 100

        # Rabin-Karp
        rabin_matches = rabin_document_match(
            original_sentences,
            submitted_sentences
        )

        rabin_score = (
            len(rabin_matches)
            / len(original_sentences)
        ) * 100

        # Jaccard
        jaccard_score, common_words = (
            jaccard_similarity(
                cleaned_original,
                cleaned_submitted
            )
        )

        # Final Score
        final_score = (
            naive_score
            + kmp_score
            + rabin_score
            + jaccard_score
        ) / 4

        # Risk Level
        if final_score < 30:
            risk_level = "🟢 Low Plagiarism"
            st.success(risk_level)

        elif final_score < 70:
            risk_level = "🟡 Moderate Similarity"
            st.warning(risk_level)

        else:
            risk_level = "🔴 High Plagiarism"
            st.error(risk_level)

        # --------------------------------
        # RESULTS
        # --------------------------------
        st.markdown(
            '<div class="section-title">'
            '📊 Detection Results'
            '</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Naive", f"{naive_score:.2f}%")
        c2.metric("KMP", f"{kmp_score:.2f}%")
        c3.metric("Rabin-Karp", f"{rabin_score:.2f}%")
        c4.metric("Jaccard", f"{jaccard_score:.2f}%")

        st.markdown(f"""
        <div class="final-card">
            <h2>Final Plagiarism Score</h2>
            <h1>{final_score:.2f}%</h1>
            <h3>{risk_level}</h3>
        </div>
        """, unsafe_allow_html=True)

        # Progress Bar
        st.progress(final_score / 100)

        # Matched Sentences
        st.markdown(
            '<div class="section-title">'
            '📝 Matched Sentences'
            '</div>',
            unsafe_allow_html=True
        )

        matched_sentences = list(
            set(
                naive_matches
                + kmp_matches
                + rabin_matches
            )
        )

        for sentence in matched_sentences:
            st.markdown(
                f'<div class="match-box">'
                f'✔ {sentence}'
                f'</div>',
                unsafe_allow_html=True
            )

        # Common Words
        st.markdown(
            '<div class="section-title">'
            '🔍 Common Words'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(", ".join(common_words))

        # Download Report
        report = f"""
Plagiarism Report

Naive Score: {naive_score:.2f}%
KMP Score: {kmp_score:.2f}%
Rabin-Karp Score: {rabin_score:.2f}%
Jaccard Score: {jaccard_score:.2f}%

Final Score: {final_score:.2f}%

Risk Level:
{risk_level}
"""

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="plagiarism_report.txt",
            mime="text/plain"
        )

    else:
        st.error(
            "Please upload both files."
        )
