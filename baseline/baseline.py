import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from labels import labels


train_df = pd.read_csv("../data/train_2/train.csv")
test_df  = pd.read_csv("../data/train_2/test.csv")

X_train = train_df["comment"].astype(str)
X_test  = test_df["comment"].astype(str)


y_train = train_df[labels].values
y_test  = test_df[labels].values


#Векторизация текста с помощью TF-IDF
#Каждый комментарий превращается в вектор из 5000 чисел -
#каждое число это вес слова (насколько оно важно в этом тексте)
vectorizer = TfidfVectorizer(
    max_features=5000,   
    ngram_range=(1, 2),  
    min_df=2             # игнорирует слова которые встречаются меньше 2 раз
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf  = vectorizer.transform(X_test)        


#Классификация
#OneVsRestClassifier - обучает отдельный классификатор
#для каждой из 7 категорий
#LogisticRegression - простой линейный классификатор
classifier = OneVsRestClassifier(
    LogisticRegression(max_iter=1000, C=1.0)
)

classifier.fit(X_train_tfidf, y_train)


#Оценка качества на тестовых данных
y_pred = classifier.predict(X_test_tfidf)

print("=" * 60)
print("Baseline модель: TF-IDF + Logistic Regression")
print("=" * 60)
print(classification_report(
    y_test,
    y_pred,
    target_names=labels,
    zero_division=0
))


#Проверка на произвольном комментарии
def predict_comment(comment):
    vec = vectorizer.transform([comment])
    pred = classifier.predict(vec)[0]
    result = [labels[i] for i, val in enumerate(pred) if val == 1]
    print(f"\nКомментарий: {comment}")
    print(f"Категории:   {', '.join(result) if result else 'Не токсичный'}")

predict_comment("Ты абсолютный идиот, как можно быть таким тупым!")
predict_comment("Спасибо за полезную информацию, очень помогло!")