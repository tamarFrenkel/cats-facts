import pandas as pd
import re

def clean_text(text: str) -> str:
    # retrun clean text
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^א-תa-zA-Z0-9\s]', '', text)
    return text.strip().lower()

def tokenize_text(text: str) -> list:
    # from text to word
    return text.split()

def clean_dataframe(df: pd.DataFrame, text_column: str) -> pd.DataFrame:
    # clean text fron table
    df[text_column] = df[text_column].apply(clean_text)
    return df
