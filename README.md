# Toxic Comment Classifier

Дипломный проект: классификация токсичных/нежелательных русскоязычных комментариев на основе fine-tuned RuBERT, с десктопным интерфейсом для модерации.

## Стек
- Python
- PyTorch, HuggingFace Transformers
- RuBERT (fine-tuning)
- PyQt6 (десктопный UI)

## Архитектура
- `train.py` — обучение модели
- `test_rubert.py` — валидация и тестирование
- `labels.py` — маппинг классов
- `interface.py`, `themes.py` — десктопный интерфейс на PyQt6
- `baseline/` — базовая модель для сравнения
- `data/` — обучающие данные

## Задача
Модель классифицирует комментарии по id,comment,Не токсичный,Токсичный,Крайне токсичный,Непристойный,Угроза,Оскорбление,Ненависть к личности
Пример датакласса:
- a1b2c3d4,"Спасибо за полезную информацию, очень пригодилось!",1,0,0,0,0,0,0

## Результаты
- Датасет: размер источника регулируется, и балансировался в ручную, н оможно афтоматизировать процесс

## Установка и запуск
\`\`\`bash
pip install -r requirements.txt
python interface.py
\`\`\`

## Скриншоты

<img width="1920" height="1079" alt="изображение" src="https://github.com/user-attachments/assets/324dc944-a156-45bb-b278-f68fb9223cc9" />

<img width="1920" height="1079" alt="изображение" src="https://github.com/user-attachments/assets/cea102b1-002d-472f-a524-7628d7f6e33d" />






 
