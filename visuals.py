import matplotlib.pyplot as plt


def plot_length_histogram(df):
    plt.hist(df['length'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of fact lengths')
    plt.xlabel('Length')
    plt.ylabel('Count')
    plt.show()

def plot_top_words(freq_df, top_n=10):
    # retrun graph with the popular word
    top_words = freq_df.head(top_n)
    plt.figure(figsize=(10, 5))
    plt.bar(top_words["word"], top_words["count"])
    plt.title("Top Words Frequency")
    plt.xlabel("Word")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
