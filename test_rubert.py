from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

#folder --- pyMy
import labels


model_name = "./results"
#model_name = "DeepPavlov/rubert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=7)

comments = [
    "Я тебя найду и прибью"
    # "Ты идиот, не знаешь ничего!",
    # "Отличная работа, спасибо за пост!"
]

inputs = tokenizer(comments, padding = True, truncation = True, return_tensors = "pt")
threshold = 0.5

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits)

# for i, comment in enumerate(comments):
#     print(f"\nКомментарий: {comment}")
#     for j, label in enumerate(labels.labels):
#         print(f"{label}: {probs[i][j].item():.2f}")



for i, comment in enumerate(comments):
    print(f"\nКомментарий: {comment}")
    positive_labels = []
    for j, label in enumerate(labels.labels):
        prob = probs[i][j].item()
        print(f"{label}: {prob:.2f}")
        if prob >= threshold:
            positive_labels.append(label)
    if positive_labels:
        print("Категории:", ", ".join(positive_labels))
    else:
        print("Категории: Нет")
        