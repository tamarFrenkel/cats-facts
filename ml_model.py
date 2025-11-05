from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def train_length_model(df,text_column='fact', target_column='length'):

    print("\n 🔧 louding")

    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(df[text_column])
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print("🤖 i do it now")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"i finish ✅ \n ")
    print(f" MSE = {mse:.2f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(y_test,y_pred, alpha=0.7)
    plt.xlabel("real length")
    plt.ylabel("Linear length")
    plt.title("השוואת ערכים אמיתיים מול תחזיות")
    plt.grid(True)
    plt.show()

    return model, vectorizer