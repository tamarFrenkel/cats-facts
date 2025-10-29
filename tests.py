import pytest
import pandas as pd
from fetcher import fetch_api_data
from processing import clean_text, tokenize_text
from analysis import aggregate_stats, compute_word_freqs

def test_fetch_api_data_ok():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_api_data(url)
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)

def test_fetch_api_data_invalid_url():
    bad_url = "https://no-such-site-xyz123.com"
    try:
        fetch_api_data(bad_url)
        assert False, "הייתה צריכה להיות שגיאה ב־requests"
    except Exception:
        assert True

def test_clean_text_removes_symbols():
    txt = "Hello!! מה נשמע???"
    result = clean_text(txt)
    assert "!" not in result
    assert "?" not in result

def test_tokenize_text():
    text = "שלום עולם טוב"
    tokens = tokenize_text(text)
    assert isinstance(tokens, list)
    assert tokens == ["שלום", "עולם", "טוב"]

def test_aggregate_stats():
    df = pd.DataFrame({"length": [1, 2, 3, 4, 5]})
    stats = aggregate_stats(df)
    assert "mean" in stats
    assert stats["mean"] == 3

def test_compute_word_freqs():
    texts = ["hello world", "hello again"]
    freqs = compute_word_freqs(texts, top_n=2)
    assert freqs[0][0] == "hello"
