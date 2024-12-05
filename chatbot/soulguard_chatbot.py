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
    "recommendation_1": {
        "examples": [
            "I feel really low", 
            "I think I'm in danger", 
            "I need help now", 
            "Life feels pointless"
        ],
        "response": "I'm sorry you're feeling this way. You're not alone. Please consider reaching out to a crisis hotline call 988 or a trusted professional for immediate support also connect to our Soulguard community support and read our blogs."
    },
    "recommendation_2": {
        "examples": [ 
            "I feel stressed", 
            "What should I do when feeling alone?", 
            "Can you help me calm down?",
            "I am not understanding what is happening with me",
            "I am feeling Bored"
        ],
        "response": "I'm here to support you. Try some calming exercises like deep breathing or mindfulness. Try to speak to yourself introspection is important sometimes, take a moment to connect with yourself. Try to connect with people who overcame join our Soulgaurd community!! ."
    },
    "recommendation_3": {
        "examples": [
            "I'm feeling sad but hopeful", 
            "What should I do to stay positive?", 
            "I need encouragement", 
            "I am feeling low",
            "I'm struggling but managing"
        ],
        "response": "It's great that you're looking for positivity! Talking to loved ones or engaging in uplifting activities like listening to music or journaling might help the best choice is to travel and explore. You can always join our tribe SouldGaurd Community. Let me know if you'd like more tips! "
    },
    "recommendation_4": {
        "examples": [
            "I'm doing okay but need self-care tips", 
            "How can I build healthy habits?", 
            "What are some ways to stay mentally strong?", 
            "Can you suggest general well-being tips?"
        ],
        "response": "You’re doing great! Try practicing gratitude, staying physically active, staying fit and maintaining a healthy routine. Connecting with friends or a support network can also make a big difference!"
    },
    "recommendation_5": {
        "examples": [
            "I'm not sure how I feel", 
            "I think I'm somewhere in between", 
            "What should I do if I'm on the edge?", 
            "I just want to cry loud",
            "My heart is so heavy and low"
        ],
        "response": "It's okay to feel unsure. Try expressing your emotions through writing or talking to someone you trust. Fitness activities and connecting with supportive communities can also help. Let me know how I can assist further!"
    },
    "thank_you": {
        "examples": ["thanks", "thank you", "appreciate it", "okay, thanks"],
        "response": "You're welcome! Happy to help and do not forget to join our SoulGaurd community because it will be a great helpful adventure."
    },

    "wrong_response": {
        "examples": ["go to hell", "not understand", "need assitance immediately", "get lost", "Kill you"],
        "response": "Sorry! unable to comprehend. Please stand by while we connect to our expert"
    },
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