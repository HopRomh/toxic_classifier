import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QComboBox
# ------------------------
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
#folder --- pyMy
import labels
import matplotlib.pyplot as plt
from themes import themes


from PyQt6.QtWidgets import QFileDialog
import csv



# def plot_probs(probs, labels):
#     plt.bar(labels, probs)
#     plt.ylabel("Вероятность")
#     plt.xticks(rotation=45)
#     plt.show()


#Модель результат обучения
max_char_comments = 10
model_name = "./results"



class ToxicApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toxic Classifier")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # кастом
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(themes.keys())
        self.theme_combo.currentTextChanged.connect(self.apply_theme)
        layout.addWidget(self.theme_combo)

        # ввод
        self.input = QLineEdit()
        self.input.setPlaceholderText("Введи комментарий...")
        layout.addWidget(self.input)

        # кнопка
        self.button = QPushButton("Классифицировать")
        self.button.clicked.connect(self.classify)
        layout.addWidget(self.button)

        # результат
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        # история
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setPlaceholderText("История последних комментариев...")
        layout.addWidget(self.history_display)

        # сохранение истории
        self.save_button = QPushButton("Save in CSV")
        self.save_button.clicked.connect(self.save_history_csv)
        layout.addWidget(self.save_button)

        # модель---
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=7)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self.model.eval()
        self.input.returnPressed.connect(self.classify)

        self.history = []


    #Сохранение темы
    def apply_theme(self, theme_name):
        if theme_name in themes:
            self.setPalette(themes[theme_name])
    #Основа
    def classify(self):
        comment = self.input.text()
        if comment == "":
            self.output.setText("Не определено")
        else:
            inputs = self.tokenizer([comment], padding=True, truncation=True, return_tensors="pt").to(self.device)
            threshold = 0.6

            with torch.no_grad():
                logits = self.model(**inputs).logits
                probs = torch.sigmoid(logits)

            result_lines = [f"Комментарий: {comment}"]
            positive_labels = []
            for j, label in enumerate(labels.labels):
                prob = probs[0][j].item()
                result_lines.append(f"{label}: {prob:.2f}")
                if prob >= threshold:
                    positive_labels.append(label)

            if positive_labels:
                result_lines.append("Категории: " + ", ".join(positive_labels))
            else:
                result_lines.append("Категории: Нет")

            self.output.setText("\n".join(result_lines))
            self.plot_probs(probs[0].cpu().numpy())

            self.hystorySave(comment, positive_labels)

    #Метод для сохранения
    def hystorySave(self, comment, positive_labels):
        self.history.append((comment, positive_labels))
        if len(self.history) > max_char_comments:
            self.history.pop(0)

        history_text = ""
        for c, cats in self.history:
            line = f"{c} -> {', '.join(cats) if cats else 'Нет'}"
            history_text += line + "\n"
        self.history_display.setText(history_text)

    #Метод для отрисовки графиков
    def plot_probs(self, probs_array):
        plt.figure(figsize=(8,4))
        plt.bar(labels.labels, probs_array, color='skyblue')
        plt.ylim(0, 1)
        plt.ylabel("Вероятность")
        plt.xticks(rotation=45, ha='right')
        plt.title("Вероятность категорий токсичности")
        plt.tight_layout()
        plt.show()

    def save_history_csv(self):
        if not self.history:
            self.history_display.setText("Пока пусто")
            return
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить CSV", "", "CSV Files (*.csv)")
        if filename:
            if not filename.endswith(".csv"):
                filename += ".csv"
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Комментарий", "Категории"])
                for comment, cats in self.history:
                    writer.writerow([comment, ", ".join(cats) if cats else "Нет"])
            self.history_display.append(f"\nИстория сохранена в {filename}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToxicApp()
    window.show()
    sys.exit(app.exec())
    
