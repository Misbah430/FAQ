# FAQ
This is a simple FAQ Chatbot built with Python, Streamlit, and fuzzy-wuzzy for fuzzy matching of user queries. It provides answers to frequently asked questions by matching user input with predefined questions stored in a JSON file.

Features

- ✅ Chat-style interface using Streamlit
- 🧠 Fuzzy matching of user questions using `fuzzywuzzy`
- 📥 Downloadable chat log
- 📬 Feedback form (stores feedback in a text file)
- 💡 Easy to customize and extend with more questions

Requirements 
•	streamlit
•	fuzzywuzzy
•	python-Levenshtein (optional but recommended for speed)
•	json (built-in)
•	datetime (built-in)

Installation 

1. Clone the Repository
   
             https://github.com/Misbah430/FAQ.git


3. Set Up Environment
   
          •	conda create -n faqbot python=3.10
          •	conda activate faqbot


4. Install Dependencies
   
         pip install -r requirements.txt
   
5. Run the App
   
         streamlit run main.py

