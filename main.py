from fetcher import fetch_api_data
from processing import clean_text, tokenize_text
from analysis import aggregate_stats, compute_word_freqs
from visuals import plot_length_histogram, plot_top_words
from ml_model import train_length_model
import pandas as pd, json, time
from automation_bot import job

def save_results(df, stats):
    df.to_csv("facts.csv", index=False)
    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    print("\n✅ Files saved: facts.csv & stats.json")


url = "https://catfact.ninja/fact"

N = int(input("how mutch facts get?"))
df = fetch_api_data(url, N)

print("✅ Data fetched successfully!")
print(df.head())

stats = aggregate_stats(df, 'fact')
print("Stats:", stats)

print("\n 🚀 i think abaut the length in fact.... ")
model, vectorizer = train_length_model(df, text_column='fact', target_column='length')

new_fact = ["Cats can jump up to six times their length."]
X_new = vectorizer.transform(new_fact)
predicted_length = model.predict(X_new)[0]
print(f"\n 🐾 ready to show think length to new fact: {predicted_length:.2f} ")

freqs = compute_word_freqs(df['fact'].tolist(), top_n=10)

plot_length_histogram(df)
plot_top_words(freqs)

save_results(df, stats)

# job()