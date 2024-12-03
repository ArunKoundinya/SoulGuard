import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords

# Download NLTK data
nltk.download('stopwords')

# Define intents
intents = {
    "greeting": {
        "examples": ["hi", "hello", "hey", "good morning", "good evening"],
        "response": "Hello! How can I assist you today?"
    },
    "goodbye": {
        "examples": ["bye", "goodbye", "see you", "take care"],
        "response": "Goodbye! Have a great day!"
    },
    "order_status": {
        "examples": ["check order", "order status", "where is my order"],
        "response": "Please provide your order ID to check the status."
    },
    "thank_you": {
        "examples": ["thanks", "thank you", "appreciate it"],
        "response": "You're welcome! Happy to help."
    }
}

# Prepare training data
data = []
labels = []

for intent, details in intents.items():
    for example in details['examples']:
        data.append(example)
        labels.append(intent)

# Train the intent classifier
pipeline = Pipeline([
    ('vectorizer', CountVectorizer(stop_words=stopwords.words('english'))),
    ('classifier', MultinomialNB())
])
pipeline.fit(data, labels)

# Chatbot response function
def chatbot_response(user_input):
    try:
        intent = pipeline.predict([user_input])[0]
        return intents[intent]["response"]
    except Exception as e:
        return "Sorry, I didn't understand that. Could you rephrase?"

# GUI Class
class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot")
        self.setGeometry(200, 200, 500, 600)

        # Layout
        self.layout = QVBoxLayout()

        # Title Label
        self.title_label = QLabel("Welcome to Chatbot", self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        # Chat display area
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("font-size: 14px;")
        self.layout.addWidget(self.chat_display)

        # User input field
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Type your message here...")
        self.layout.addWidget(self.user_input)

        # Send button
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_send)
        self.send_button.setStyleSheet("background-color: #007BFF; color: white; font-size: 14px;")
        self.layout.addWidget(self.send_button)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def handle_send(self):
        user_message = self.user_input.text().strip()
        if user_message:
            self.chat_display.append(f"You: {user_message}")
            bot_reply = chatbot_response(user_message)
            self.chat_display.append(f"Soul Guard: {bot_reply}\n")
            self.user_input.clear()

# Main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatbotApp()
    main_window.show()
    sys.exit(app.exec_())