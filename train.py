import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader    
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.optim import AdamW
from labels import labels  


MODEL_NAME = "DeepPavlov/rubert-base-cased"
BATCH_SIZE = 8
EPOCHS = 8
LR = 3e-5
DEVICE = "cpu" # "cuda" if torch.cuda.is_available() else "cpu"

# Загрузка данных
train_df = pd.read_csv("data/dataset_ready/train.csv")
val_df = pd.read_csv("data/dataset_ready/val.csv")



def preprocess_labels(df):
    return df[labels].astype(float)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

class CommentDataset(Dataset):
    def __init__(self, df, tokenizer):
        self.comments = df["comment"].tolist()
        self.labels = preprocess_labels(df).values
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.comments)

    def __getitem__(self, idx):
        tokenized = self.tokenizer(
            self.comments[idx],
            padding="max_length",
            truncation=True,
            max_length=128,
            return_tensors="pt"
        )
        item = {k: v.squeeze(0) for k, v in tokenized.items()}
        item["labels"] = torch.tensor(self.labels[idx], dtype=torch.float)
        return item



train_dataset = CommentDataset(train_df, tokenizer)
val_dataset = CommentDataset(val_df, tokenizer)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)


model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(labels)
)

model.to(DEVICE)
optimizer = AdamW(model.parameters(), lr=LR)
criterion = torch.nn.BCEWithLogitsLoss()


for epoch in range(EPOCHS):
    model.train()
    total_loss = 0
    for batch in train_loader:
        optimizer.zero_grad()
        inputs = {k: v.to(DEVICE) for k, v in batch.items() if k != "labels"}
        labels_tensor = batch["labels"].to(DEVICE)
        outputs = model(**inputs)
        loss = criterion(outputs.logits, labels_tensor)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}/{EPOCHS} - Train Loss: {total_loss/len(train_loader):.4f}")


    model.eval()
    val_loss = 0
    with torch.no_grad():
        for batch in val_loader:
            inputs = {k: v.to(DEVICE) for k, v in batch.items() if k != "labels"}
            labels_tensor = batch["labels"].to(DEVICE)
            outputs = model(**inputs)
            loss = criterion(outputs.logits, labels_tensor)
            val_loss += loss.item()
    print(f"Epoch {epoch+1}/{EPOCHS} - Val Loss: {val_loss/len(val_loader):.4f}")

model.save_pretrained("results")        
tokenizer.save_pretrained("results")    

