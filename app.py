import streamlit as st
from collections import Counter
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="BIOINFORMATICS SEQUENCE ANALYZER",
    page_icon="🧬",
    layout="wide"

    
)
# =========================
# HEADER IMAGE
# =========================
st.image("assets/gc_chart.png.png", use_container_width=True)


# ============================================================
# CUSTOM CSS
# ============================================================

# ============================================================
# PREMIUM BIOINFORMATICS UI
# ============================================================

st.markdown("""

<style>

[data-testid="stImage"] img {
    width: 100%;
    height: auto !important;
    object-fit: contain !important;
}
/* Main Background */
.stApp {
     
    background: linear-gradient(135deg, #020617, #0f172a, #172554);
    color: white;
}
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 229, 255, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(124, 58, 237, 0.12),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #050816 0%,
            #08111f 50%,
            #050816 100%
        );

    color: #f1f5f9;
}


/* Main Content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}


/* Main Heading */
.big-title {
    font-size: 52px;
    font-weight: 900;
    text-align: center;
    letter-spacing: -1px;

    background: linear-gradient(
        90deg,
        #22d3ee,
        #60a5fa,
        #a78bfa
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 5px;
}


/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 30px;
}


/* Section Headings */
h1, h2, h3 {
    color: #e2e8f0 !important;
    font-weight: 750 !important;
}


/* Sidebar */
section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #070b17,
            #0b1220
        );

    border-right: 1px solid
        rgba(148, 163, 184, 0.12);
}


/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}


/* Metric Cards */
div[data-testid="stMetric"] {

    background:
        rgba(15, 23, 42, 0.72);

    border: 1px solid
        rgba(56, 189, 248, 0.18);

    border-radius: 18px;

    padding: 18px;

    box-shadow:
        0 10px 30px
        rgba(0, 0, 0, 0.25);
}


/* Metric Number */
div[data-testid="stMetricValue"] {
    color: #67e8f9;
    font-weight: 800;
}


/* Buttons */
.stButton > button {

    width: 100%;

    border-radius: 12px;

    border: 1px solid
        rgba(34, 211, 238, 0.35);

    background:
        linear-gradient(
            135deg,
            rgba(8, 145, 178, 0.25),
            rgba(124, 58, 237, 0.25)
        );

    color: #f8fafc;

    font-weight: 700;

    padding: 0.65rem 1rem;

    transition: all 0.25s ease;
}


/* Button Hover */
.stButton > button:hover {

    border-color: #22d3ee;

    background:
        linear-gradient(
            135deg,
            rgba(8, 145, 178, 0.45),
            rgba(124, 58, 237, 0.45)
        );

    transform: translateY(-2px);

    box-shadow:
        0 8px 25px
        rgba(34, 211, 238, 0.15);
}


/* Text Area */
textarea {

    background-color:
        rgba(15, 23, 42, 0.75) !important;

    color: #f8fafc !important;

    border: 1px solid
        rgba(148, 163, 184, 0.20) !important;

    border-radius: 14px !important;
}


/* Text Input */
input {

    background-color:
        rgba(15, 23, 42, 0.75) !important;

    color: #f8fafc !important;
}


/* Selectbox */
div[data-baseweb="select"] > div {

    background-color:
        rgba(15, 23, 42, 0.80) !important;

    border-radius: 12px !important;
}


/* File uploader */
section[data-testid="stFileUploader"] {

    background:
        rgba(15, 23, 42, 0.55);

    border: 1px dashed
        rgba(34, 211, 238, 0.35);

    border-radius: 16px;

    padding: 10px;
}


/* Dataframes */
div[data-testid="stDataFrame"] {

    border-radius: 14px;

    overflow: hidden;

    border: 1px solid
        rgba(148, 163, 184, 0.15);
}


/* Alerts */
div[data-testid="stAlert"] {

    border-radius: 14px;
}


/* Images */
img {

    border-radius: 16px;

    box-shadow:
        0 12px 35px
        rgba(0, 0, 0, 0.35);
}


/* Divider */
hr {

    border-color:
        rgba(148, 163, 184, 0.12);
}


/* Code Blocks */
code {

    border-radius: 10px;
}


/* Footer */
.footer {

    text-align: center;

    color: #64748b;

    padding: 30px;

    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="big-title">🧬 Bioinformatics Sequence Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze DNA, RNA and protein sequences with interactive visualization'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clean_sequence(sequence):

    if sequence is None:
        return ""

    return (
        sequence
        .upper()
        .replace(" ", "")
        .replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
    )


def validate_dna(sequence):

    valid_bases = set("ATGC")

    return (
        len(sequence) > 0
        and set(sequence).issubset(valid_bases)
    )


def calculate_gc(sequence):

    if len(sequence) == 0:
        return 0

    gc = sequence.count("G") + sequence.count("C")

    return (gc / len(sequence)) * 100


def calculate_at(sequence):

    if len(sequence) == 0:
        return 0

    at = sequence.count("A") + sequence.count("T")

    return (at / len(sequence)) * 100


def reverse_complement(sequence):

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    return "".join(
        complement.get(base, base)
        for base in reversed(sequence)
    )


def dna_to_rna(sequence):

    return sequence.replace("T", "U")


def parse_fasta(text):

    sequences = {}

    current_id = None
    current_sequence = []

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):

            if current_id is not None:
                sequences[current_id] = "".join(
                    current_sequence
                )

            current_id = line[1:].strip()
            current_sequence = []

        else:

            current_sequence.append(line)

    if current_id is not None:
        sequences[current_id] = "".join(
            current_sequence
        )

    return sequences


def translate_dna(sequence):

    codon_table = {

        "TTT": "F", "TTC": "F",
        "TTA": "L", "TTG": "L",

        "TCT": "S", "TCC": "S",
        "TCA": "S", "TCG": "S",

        "TAT": "Y", "TAC": "Y",
        "TAA": "*", "TAG": "*",

        "TGT": "C", "TGC": "C",
        "TGA": "*", "TGG": "W",

        "CTT": "L", "CTC": "L",
        "CTA": "L", "CTG": "L",

        "CCT": "P", "CCC": "P",
        "CCA": "P", "CCG": "P",

        "CAT": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",

        "CGT": "R", "CGC": "R",
        "CGA": "R", "CGG": "R",

        "ATT": "I", "ATC": "I",
        "ATA": "I", "ATG": "M",

        "ACT": "T", "ACC": "T",
        "ACA": "T", "ACG": "T",

        "AAT": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",

        "AGT": "S", "AGC": "S",
        "AGA": "R", "AGG": "R",

        "GTT": "V", "GTC": "V",
        "GTA": "V", "GTG": "V",

        "GCT": "A", "GCC": "A",
        "GCA": "A", "GCG": "A",

        "GAT": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",

        "GGT": "G", "GGC": "G",
        "GGA": "G", "GGG": "G"
    }

    protein = ""

    for i in range(0, len(sequence) - 2, 3):

        codon = sequence[i:i+3]

        protein += codon_table.get(codon, "X")

    return protein


def hamming_distance(seq1, seq2):

    length = min(len(seq1), len(seq2))

    distance = sum(
        seq1[i] != seq2[i]
        for i in range(length)
    )

    distance += abs(len(seq1) - len(seq2))

    return distance


def sequence_similarity(seq1, seq2):

    if len(seq1) == 0 or len(seq2) == 0:
        return 0

    length = min(len(seq1), len(seq2))

    matches = sum(
        seq1[i] == seq2[i]
        for i in range(length)
    )

    return (matches / length) * 100


def amino_acid_properties(protein):

    masses = {

        "A": 89.09,
        "R": 174.20,
        "N": 132.12,
        "D": 133.10,
        "C": 121.15,
        "E": 147.13,
        "Q": 146.15,
        "G": 75.07,
        "H": 155.16,
        "I": 131.17,
        "L": 131.17,
        "K": 146.19,
        "M": 149.21,
        "F": 165.19,
        "P": 115.13,
        "S": 105.09,
        "T": 119.12,
        "W": 204.23,
        "Y": 181.19,
        "V": 117.15
    }

    molecular_weight = sum(
        masses.get(aa, 0)
        for aa in protein
    )

    return molecular_weight


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧬 Analyzer Menu")

menu = st.sidebar.radio(
    "Select Analysis",
    [
        "🏠 Home",
        "🧬 DNA Analyzer",
        "📁 FASTA Analyzer",
        "🧪 Protein Analysis",
        "📊 Sequence Statistics",
        "📈 GC/AT Visualization",
        "🔄 Sequence Comparison",
        "🔎 Subsequence Search",
        "🧬 DNA → Protein",
        "🧬 Mutation Analysis",
        "🌐 Real Biological Data",
        "📊 Advanced Visualization"
    ]
)


# ============================================================
# HOME
# ============================================================

if menu == "🏠 Home":

    st.header("🧬 Welcome to Bioinformatics Sequence Analyzer")

    st.write(
        """
        This web application combines multiple bioinformatics
        sequence analysis techniques into one platform.
        """
    )

    st.success(
        "Day 1–15 Bioinformatics Project Dashboard"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Analysis Modules",
            "12+"
        )

    with col2:

        st.metric(
            "Sequence Types",
            "DNA / RNA / Protein"
        )

    with col3:

        st.metric(
            "Visualization",
            "Interactive"
        )

    st.divider()

    st.subheader("🚀 Project Features")

    features = [

        "Basic DNA analysis",

        "FASTA file handling",

        "Sequence statistics",

        "Protein sequence analysis",

        "GC / AT visualization",

        "Sequence comparison",

        "Subsequence search",

        "DNA → Protein translation",

        "Mutation analysis",

        "Real biological FASTA data",

        "Advanced visualization",

        "Downloadable results"
    ]

    for feature in features:

        st.write("✅", feature)


# ============================================================
# DNA ANALYZER
# ============================================================

elif menu == "🧬 DNA Analyzer":

    st.header("🧬 Basic DNA Analyzer")

    sequence = st.text_area(
        "Enter DNA Sequence",
        placeholder="Example: ATGCGTACGATCG",
        height=180
    )

    if st.button(
        "🔍 Analyze DNA",
        use_container_width=True
    ):

        sequence = clean_sequence(sequence)

        if not sequence:

            st.warning(
                "Please enter a DNA sequence."
            )

        elif not validate_dna(sequence):

            st.error(
                "Invalid DNA sequence! "
                "Use only A, T, G and C."
            )

        else:

            st.success(
                "Sequence analyzed successfully!"
            )

            length = len(sequence)

            counts = Counter(sequence)

            gc = calculate_gc(sequence)

            at = calculate_at(sequence)

            st.subheader("📊 Results")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                    "Length",
                    length
                )

            with c2:
                st.metric(
                    "GC Content",
                    f"{gc:.2f}%"
                )

            with c3:
                st.metric(
                    "AT Content",
                    f"{at:.2f}%"
                )

            st.divider()

            st.subheader(
                "🧬 Nucleotide Count"
            )

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric(
                    "A",
                    counts["A"]
                )

            with c2:
                st.metric(
                    "T",
                    counts["T"]
                )

            with c3:
                st.metric(
                    "G",
                    counts["G"]
                )

            with c4:
                st.metric(
                    "C",
                    counts["C"]
                )

            st.divider()

            st.subheader(
                "🔄 Sequence Processing"
            )

            st.write(
                "**RNA Sequence:**",
                dna_to_rna(sequence)
            )

            st.write(
                "**Reverse Complement:**"
            )

            st.code(
                reverse_complement(sequence)
            )

            st.subheader(
                "🔬 Input Sequence"
            )

            st.code(sequence)


# ============================================================
# FASTA ANALYZER
# ============================================================

elif menu == "📁 FASTA Analyzer":

    st.header("📁 FASTA File Analyzer")

    uploaded_file = st.file_uploader(
        "Upload FASTA file",
        type=["fasta", "fa", "txt"]
    )

    if uploaded_file is not None:

        text = uploaded_file.read().decode(
            "utf-8"
        )

        fasta_sequences = parse_fasta(text)

        if fasta_sequences:

            st.success(
                f"{len(fasta_sequences)} sequence(s) found!"
            )

            rows = []

            for seq_id, seq in fasta_sequences.items():

                seq = clean_sequence(seq)

                rows.append(
                    {
                        "ID": seq_id,
                        "Length": len(seq),
                        "GC %": round(
                            calculate_gc(seq),
                            2
                        ),
                        "AT %": round(
                            calculate_at(seq),
                            2
                        )
                    }
                )

            df = pd.DataFrame(rows)

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader(
                "🧬 FASTA Sequences"
            )

            for seq_id, seq in fasta_sequences.items():

                with st.expander(
                    f"🔹 {seq_id}"
                ):

                    st.write(
                        f"Length: {len(seq)} bp"
                    )

                    st.code(seq)

            csv_data = df.to_csv(
                index=False
            )

            st.download_button(
                "📥 Download Results CSV",
                csv_data,
                "fasta_analysis.csv",
                "text/csv"
            )

        else:

            st.error(
                "Could not find valid FASTA sequences."
            )


# ============================================================
# PROTEIN ANALYSIS
# ============================================================

elif menu == "🧪 Protein Analysis":

    st.header("🧪 Protein Sequence Analysis")

    protein = st.text_area(
        "Enter Protein Sequence",
        placeholder="Example: MKTAYIAKQRQISFVKSHFSRQ",
        height=150
    )

    if st.button(
        "🔬 Analyze Protein",
        use_container_width=True
    ):

        protein = clean_sequence(protein)

        valid_amino_acids = set(
            "ACDEFGHIKLMNPQRSTVWY"
        )

        if not protein:

            st.warning(
                "Enter a protein sequence."
            )

        elif not set(protein).issubset(
            valid_amino_acids
        ):

            st.error(
                "Invalid amino acid sequence."
            )

        else:

            aa_count = Counter(protein)

            molecular_weight = (
                amino_acid_properties(
                    protein
                )
            )

            st.success(
                "Protein analyzed successfully!"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Length",
                    f"{len(protein)} aa"
                )

            with c2:

                st.metric(
                    "Approx. Molecular Weight",
                    f"{molecular_weight:.2f} Da"
                )

            st.subheader(
                "🧬 Amino Acid Composition"
            )

            aa_df = pd.DataFrame(
                {
                    "Amino Acid":
                        list(aa_count.keys()),

                    "Count":
                        list(aa_count.values())
                }
            )

            st.bar_chart(
                aa_df.set_index(
                    "Amino Acid"
                )
            )

            st.subheader(
                "🔬 Protein Sequence"
            )

            st.code(protein)


# ============================================================
# SEQUENCE STATISTICS
# ============================================================

elif menu == "📊 Sequence Statistics":

    st.header(
        "📊 Sequence Statistics"
    )

    input_sequences = st.text_area(
        "Enter multiple DNA sequences "
        "(one per line)",
        height=200
    )

    if st.button(
        "📊 Calculate Statistics"
    ):

        sequences = [
            clean_sequence(x)
            for x in input_sequences.splitlines()
            if x.strip()
        ]

        if not sequences:

            st.warning(
                "Enter at least one sequence."
            )

        else:

            rows = []

            for i, seq in enumerate(
                sequences,
                start=1
            ):

                rows.append(
                    {
                        "Sequence":
                            f"Seq{i}",

                        "Length":
                            len(seq),

                        "A":
                            seq.count("A"),

                        "T":
                            seq.count("T"),

                        "G":
                            seq.count("G"),

                        "C":
                            seq.count("C"),

                        "GC %":
                            round(
                                calculate_gc(seq),
                                2
                            ),

                        "AT %":
                            round(
                                calculate_at(seq),
                                2
                            )
                    }
                )

            df = pd.DataFrame(rows)

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader(
                "📈 Sequence Length Distribution"
            )

            st.bar_chart(
                df.set_index("Sequence")[
                    "Length"
                ]
            )


# ============================================================
# GC / AT VISUALIZATION
# ============================================================

elif menu == "📈 GC/AT Visualization":

    st.header(
        "📈 GC / AT Visualization"
    )

    sequence = st.text_area(
        "Enter DNA Sequence",
        placeholder="ATGCGTACGATCG"
    )

    if st.button(
        "📊 Generate Visualization"
    ):

        sequence = clean_sequence(sequence)

        if not validate_dna(sequence):

            st.error(
                "Please enter a valid DNA sequence."
            )

        else:

            counts = Counter(sequence)

            gc = calculate_gc(sequence)

            at = calculate_at(sequence)

            # Nucleotide count chart

            fig1, ax1 = plt.subplots()

            bases = ["A", "T", "G", "C"]

            values = [
                counts["A"],
                counts["T"],
                counts["G"],
                counts["C"]
            ]

            ax1.bar(
                bases,
                values
            )

            ax1.set_title(
                "Nucleotide Count"
            )

            ax1.set_xlabel(
                "Nucleotide"
            )

            ax1.set_ylabel(
                "Count"
            )

            st.pyplot(fig1)

            # GC / AT pie chart

            fig2, ax2 = plt.subplots()

            ax2.pie(
                [gc, at],
                labels=["GC", "AT"],
                autopct="%1.1f%%"
            )

            ax2.set_title(
                "GC vs AT Content"
            )

            st.pyplot(fig2)

            # GC distribution

            gc_values = []

            window = 20

            if len(sequence) >= window:

                for i in range(
                    len(sequence) - window + 1
                ):

                    sub = sequence[
                        i:i + window
                    ]

                    gc_values.append(
                        calculate_gc(sub)
                    )

                fig3, ax3 = plt.subplots()

                ax3.plot(
                    gc_values
                )

                ax3.set_title(
                    "GC Content Distribution"
                )

                ax3.set_xlabel(
                    "Window Position"
                )

                ax3.set_ylabel(
                    "GC %"
                )

                st.pyplot(fig3)

            # Existing image if available

            image_path = Path(
                "assets/gc_chart.png"
            )

            if image_path.exists():

                st.subheader(
                    "🖼️ Saved GC Chart"
                )

                st.image(
                    str(image_path),
                    caption="GC Content Analysis",
                    use_container_width=True
                )


# ============================================================
# SEQUENCE COMPARISON
# ============================================================

elif menu == "🔄 Sequence Comparison":

    st.header(
        "🔄 DNA Sequence Comparison"
    )

    seq1 = st.text_input(
        "Reference Sequence"
    )

    seq2 = st.text_input(
        "Query Sequence"
    )

    if st.button(
        "🔍 Compare Sequences"
    ):

        seq1 = clean_sequence(seq1)
        seq2 = clean_sequence(seq2)

        if not validate_dna(seq1) or not validate_dna(seq2):

            st.error(
                "Enter valid DNA sequences."
            )

        else:

            similarity = sequence_similarity(
                seq1,
                seq2
            )

            distance = hamming_distance(
                seq1,
                seq2
            )

            c1, c2 = st.columns(2)

            with c1:

                st.metric(
                    "Similarity",
                    f"{similarity:.2f}%"
                )

            with c2:

                st.metric(
                    "Hamming Distance",
                    distance
                )

            st.subheader(
                "Alignment Comparison"
            )

            length = min(
                len(seq1),
                len(seq2)
            )

            match_line = ""

            for i in range(length):

                if seq1[i] == seq2[i]:

                    match_line += "|"

                else:

                    match_line += "."

            st.code(
                seq1[:length]
                + "\n"
                + match_line
                + "\n"
                + seq2[:length]
            )


# ============================================================
# SUBSEQUENCE SEARCH
# ============================================================

elif menu == "🔎 Subsequence Search":

    st.header(
        "🔎 Subsequence / Motif Search"
    )

    sequence = st.text_input(
        "DNA Sequence"
    )

    motif = st.text_input(
        "Motif / Subsequence",
        value="ATG"
    )

    if st.button(
        "🔎 Search Motif"
    ):

        sequence = clean_sequence(sequence)
        motif = clean_sequence(motif)

        if not sequence or not motif:

            st.warning(
                "Enter both sequence and motif."
            )

        else:

            positions = []

            start = 0

            while True:

                position = sequence.find(
                    motif,
                    start
                )

                if position == -1:
                    break

                positions.append(
                    position
                )

                start = position + 1

            if positions:

                st.success(
                    f"Found {len(positions)} occurrence(s)."
                )

                st.write(
                    "Positions (0-based):",
                    positions
                )

            else:

                st.info(
                    "Motif not found."
                )


# ============================================================
# DNA → PROTEIN
# ============================================================

elif menu == "🧬 DNA → Protein":

    st.header(
        "🧬 DNA → Protein Translation"
    )

    dna = st.text_area(
        "Enter DNA Sequence",
        placeholder="ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
    )

    frame = st.selectbox(
        "Reading Frame",
        [0, 1, 2]
    )

    if st.button(
        "🧬 Translate"
    ):

        dna = clean_sequence(dna)

        if not validate_dna(dna):

            st.error(
                "Enter a valid DNA sequence."
            )

        else:

            translated = translate_dna(
                dna[frame:]
            )

            st.success(
                "Translation completed!"
            )

            st.subheader(
                "Protein Sequence"
            )

            st.code(
                translated
            )

            st.metric(
                "Amino Acids",
                len(translated)
            )

            stop_position = translated.find("*")

            if stop_position != -1:

                st.info(
                    f"Stop codon found at "
                    f"amino acid position "
                    f"{stop_position + 1}"
                )


# ============================================================
# MUTATION ANALYSIS
# ============================================================

elif menu == "🧬 Mutation Analysis":

    st.header(
        "🧬 Mutation Analysis"
    )

    reference = st.text_input(
        "Reference Sequence"
    )

    query = st.text_input(
        "Query / Mutated Sequence"
    )

    if st.button(
        "🔬 Analyze Mutations"
    ):

        reference = clean_sequence(
            reference
        )

        query = clean_sequence(
            query
        )

        if not reference or not query:

            st.warning(
                "Enter both sequences."
            )

        else:

            mutations = []

            max_length = max(
                len(reference),
                len(query)
            )

            for i in range(max_length):

                ref_base = (
                    reference[i]
                    if i < len(reference)
                    else "-"
                )

                query_base = (
                    query[i]
                    if i < len(query)
                    else "-"
                )

                if ref_base != query_base:

                    if ref_base == "-":

                        mutation_type = "Insertion"

                    elif query_base == "-":

                        mutation_type = "Deletion"

                    else:

                        mutation_type = "Substitution"

                    mutations.append(
                        {
                            "Position":
                                i + 1,

                            "Reference":
                                ref_base,

                            "Query":
                                query_base,

                            "Mutation":
                                mutation_type
                        }
                    )

            if mutations:

                st.error(
                    f"{len(mutations)} mutation(s) found."
                )

                mutation_df = pd.DataFrame(
                    mutations
                )

                st.dataframe(
                    mutation_df,
                    use_container_width=True
                )

                csv = mutation_df.to_csv(
                    index=False
                )

                st.download_button(
                    "📥 Download Mutation Report",
                    csv,
                    "mutation_report.csv",
                    "text/csv"
                )

            else:

                st.success(
                    "No mutations found."
                )


# ============================================================
# REAL BIOLOGICAL DATA
# ============================================================

elif menu == "🌐 Real Biological Data":

    st.header(
        "🌐 Real Biological Data Analysis"
    )

    st.info(
        """
        Upload FASTA sequences obtained from databases
        such as NCBI or UniProt and analyze them here.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload biological FASTA data",
        type=["fasta", "fa", "txt"],
        key="biological_fasta"
    )

    if uploaded_file is not None:

        text = uploaded_file.read().decode(
            "utf-8"
        )

        sequences = parse_fasta(text)

        if sequences:

            st.success(
                f"{len(sequences)} biological sequence(s) loaded."
            )

            rows = []

            for seq_id, seq in sequences.items():

                seq = clean_sequence(seq)

                rows.append(
                    {
                        "ID":
                            seq_id,

                        "Length":
                            len(seq),

                        "GC Content":
                            round(
                                calculate_gc(seq),
                                2
                            )
                    }
                )

            df = pd.DataFrame(rows)

            st.dataframe(
                df,
                use_container_width=True
            )

            st.subheader(
                "📈 Biological Sequence Lengths"
            )

            st.bar_chart(
                df.set_index("ID")[
                    "Length"
                ]
            )

            st.subheader(
                "🧬 Sequence Data"
            )

            for seq_id, seq in sequences.items():

                with st.expander(seq_id):

                    st.code(seq)


# ============================================================
# ADVANCED VISUALIZATION
# ============================================================

elif menu == "📊 Advanced Visualization":

    st.header(
        "📊 Advanced Visualization"
    )

    sequences_input = st.text_area(
        "Enter multiple DNA sequences "
        "(one per line)",
        height=200
    )

    if st.button(
        "📊 Generate Advanced Visualizations"
    ):

        sequences = [
            clean_sequence(x)
            for x in sequences_input.splitlines()
            if x.strip()
        ]

        valid_sequences = [
            x for x in sequences
            if validate_dna(x)
        ]

        if not valid_sequences:

            st.error(
                "Enter valid DNA sequences."
            )

        else:

            # ---------------------------------------------
            # Sequence Length Distribution
            # ---------------------------------------------

            st.subheader(
                "📏 Sequence Length Distribution"
            )

            lengths = [
                len(seq)
                for seq in valid_sequences
            ]

            fig1, ax1 = plt.subplots()

            ax1.hist(
                lengths,
                bins=8
            )

            ax1.set_title(
                "Sequence Length Distribution"
            )

            ax1.set_xlabel(
                "Length"
            )

            ax1.set_ylabel(
                "Frequency"
            )

            st.pyplot(fig1)

            # ---------------------------------------------
            # GC Content Distribution
            # ---------------------------------------------

            st.subheader(
                "🧬 GC Content Distribution"
            )

            gc_values = [
                calculate_gc(seq)
                for seq in valid_sequences
            ]

            fig2, ax2 = plt.subplots()

            ax2.hist(
                gc_values,
                bins=8
            )

            ax2.set_title(
                "GC Content Distribution"
            )

            ax2.set_xlabel(
                "GC Content (%)"
            )

            ax2.set_ylabel(
                "Frequency"
            )

            st.pyplot(fig2)

            # ---------------------------------------------
            # Similarity Matrix
            # ---------------------------------------------

            st.subheader(
                "🔥 Sequence Similarity Matrix"
            )

            n = len(valid_sequences)

            matrix = np.zeros(
                (n, n)
            )

            for i in range(n):

                for j in range(n):

                    matrix[i, j] = (
                        sequence_similarity(
                            valid_sequences[i],
                            valid_sequences[j]
                        )
                    )

            fig3, ax3 = plt.subplots()

            im = ax3.imshow(
                matrix,
                cmap="viridis",
                vmin=0,
                vmax=100
            )

            ax3.set_title(
                "Sequence Similarity Heatmap"
            )

            ax3.set_xlabel(
                "Sequence"
            )

            ax3.set_ylabel(
                "Sequence"
            )

            fig3.colorbar(
                im,
                ax=ax3,
                label="Similarity (%)"
            )

            st.pyplot(fig3)

            # ---------------------------------------------
            # Summary Table
            # ---------------------------------------------

            st.subheader(
                "📋 Advanced Analysis Summary"
            )

            advanced_df = pd.DataFrame(
                {
                    "Sequence":
                        [
                            f"Seq{i+1}"
                            for i in range(n)
                        ],

                    "Length":
                        lengths,

                    "GC %":
                        [
                            round(x, 2)
                            for x in gc_values
                        ]
                }
            )

            st.dataframe(
                advanced_df,
                use_container_width=True
            )

            # ---------------------------------------------
            # Download
            # ---------------------------------------------

            csv = advanced_df.to_csv(
                index=False
            )

            st.download_button(
                "📥 Download Advanced Results",
                csv,
                "advanced_analysis.csv",
                "text/csv"
            )


# ============================================================
# FOOTER
# ============================================================


# ============================================================
# ABOUT THE DEVELOPER
# ============================================================

st.markdown("---")

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(15,23,42,0.9), rgba(30,41,59,0.8));
    padding: 35px;
    border-radius: 22px;
    border: 1px solid rgba(34,211,238,0.25);
    text-align: center;
    margin-top: 40px;
">

<h2 style="color:#67e8f9; margin-bottom:5px;">
👨‍💻 About the Developer
</h2>

<h1 style="margin-bottom:10px;">
Hi, I'm Sujeet Kumar 👋
</h1>

<p style="font-size:17px; color:#cbd5e1; line-height:1.7;">
I'm a Biotechnology student passionate about 
<b>Bioinformatics, Computational Biology, Programming</b>
and <b>Biological Data Analysis</b>.
</p>

<p style="font-size:16px; color:#94a3b8;">
I built this Bioinformatics Sequence Analyzer to combine
biology with Python and create a practical tool for
sequence analysis and visualization.
</p>

<br>

<p style="font-size:17px;">
🧬 Bioinformatics &nbsp;&nbsp; | &nbsp;&nbsp;
🔬 Computational Biology &nbsp;&nbsp; | &nbsp;&nbsp;
💻 Python &nbsp;&nbsp; | &nbsp;&nbsp;
📊 Data Analysis
</p>

<br>

<p style="color:#67e8f9; font-size:18px; font-weight:600;">
From Biological Data → Computational Insights.
</p>

</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <div style="text-align:center">

    🧬 **Bioinformatics Sequence Analyzer**

    Day 1–15 Learning & Development Project

    Built with **Python + Streamlit + Sujeet'MIND**

    </div>
    """,
    unsafe_allow_html=True
)