[![Python application test with Github Actions](https://github.com/ArunKoundinya/SoulGuard/actions/workflows/main.yml/badge.svg)](https://github.com/ArunKoundinya/SoulGuard/actions/workflows/main.yml)

[![pages-build-deployment](https://github.com/ArunKoundinya/SoulGuard/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ArunKoundinya/SoulGuard/actions/workflows/pages/pages-build-deployment)

### SoulGuard: Depression-Induced Suicide Prevention Application

Why SoulGuard?
Suicides are a global crisis, with over 700,000 lives lost annually. Root causes include social isolation, financial distress, relationship struggles, and mental health disorders, with depression as a leading contributor. Depression often leaves individuals feeling hopeless and emotionally overwhelmed, and societal stigma or lack of resources prevents many from seeking help in time.

Depression is a mental health condition marked by persistent sadness, loss of interest, and fatigue. Research including the seminal studies by Beck and colleagues, highlights a strong link between depression and suicide, as untreated depression can lead to suicidal ideation due to feelings of hopelessness. Addressing this connection is crucial to preventing tragedies.

Soul Guard addresses this by leveraging AI to analyze social media and user input, detecting depression indicators and differentiating between general symptoms and suicide risks. With its dual-user model—“For You” and “For Whom You Care”—the app provides tailored interventions, emotional tracking, and direct access to resources, empowering users to take proactive steps and save lives.

### How the App is Built

#### 1. Front-End Overview
The SoulGuard Django Project front-end is designed to support mental health by creating a positive and user-friendly interface. Inspired by the 988 website, it features a professional layout with carefully selected header and footer formatting. Colors were chosen using a color contrast analyzer to meet accessibility standards (4:1 ratio), fostering a comforting visual experience.

The landing page is divided into two sections: For You, focusing on personal well-being, and To Whom You Care, supporting loved ones. Custom visuals and a logo were crafted using Canva and sourced from Pixabay, ensuring an uplifting and professional design. Privacy and security are integral, with Terms and Conditions, age restrictions (18+), and user authentication required to access features like posting. This front-end design combines aesthetics and functionality to create a safe and engaging user experience.

#### 2. Back-End Models Overview
To deliver accurate and insightful results, our backend leverages advanced machine learning models and natural language processing techniques. The workflow includes:

Suicide Model :
The suicide detection model is designed with three BiLSTM layers, followed by a flattening layer to process the output. This is then passed through a series of dense layers before reaching the output layer.

Sentiment Model
The sentiment model is a hybrid approach combining TextBlob, VADER sentiment analysis, custom-defined words, and worry-related words derived from the NRC lexicon. The final sentiment score is calculated as a weighted average of these components.

#### 3. Chatbot
The chatbot is designed to provide users with quick and seamless virtual assistance, with the ultimate goal of facilitating a connection to a real agent, such as a therapist, when necessary.

Built with customized intents, the chatbot leverages NLP techniques, including a Count Vectorizer and a Multinomial Naive Bayes classifier, to accurately identify user intents based on their queries. This enables the chatbot to address user questions effectively using predefined responses tailored to their needs.

Visit the webpage for detail explanation https://arunkoundinya.github.io/SoulGuard/ 
