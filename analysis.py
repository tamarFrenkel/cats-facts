import pandas as pd
from collections import Counter

def aggregate_stats(df: pd.DataFrame, text_column: str) -> dict:
    # statics
    total_rows = len(df)
    avg_length = df[text_column].apply(lambda x: len(x.split())).mean()
    return {"rows": total_rows, "avg_words_per_row": avg_length}


def compute_word_freqs(texts, top_n=10) -> pd.DataFrame:
    if isinstance(texts, pd.Series):
        texts = texts.tolist()
    elif isinstance(texts, pd.DataFrame):
        if 'fact' in texts.columns:
            texts = texts['fact'].tolist()

    all_words = " ".join(texts).split()
    counts = Counter(all_words)
    freq_df = pd.DataFrame(counts.items(), columns=["word", "count"])
    return freq_df.sort_values(by="count", ascending=False).head(top_n)
