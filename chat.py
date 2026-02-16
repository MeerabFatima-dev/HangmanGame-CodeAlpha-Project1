def get_response(user_input):
    rules = {
        # Greetings
        ("hi", "hello", "hey", "assalamualaikum"): 
        "Hello! How can I help you today? 😊",

        # Identity
        ("your name", "who are you"): 
        "I'm RuleBot, a rule-based chatbot built in Python.",

        # Well-being
        ("how are you", "how r u"): 
        "I'm doing great! Thanks for asking 🌸",

        # Ask something
        ("ask a question", "ask something"):
        "Yes, I can answer simple questions.",

        # Help
        ("help", "support"): 
        "I can answer FAQs about Python, chatbots, and basic CS concepts.",

        # Python FAQs
        ("what is python",): 
        "Python is a high-level, easy-to-learn programming language.",

        ("python uses", "why python"): 
        "Python is used in web development, data science, AI, automation, and more.",

        ("python easy", "is python easy"): 
        "Yes! Python is beginner-friendly and very readable.",

        # Chatbot FAQs
        ("what is chatbot",): 
        "A chatbot is a program that simulates human conversation.",

        ("rule based chatbot",): 
        "A rule-based chatbot replies using predefined rules and keywords.",

        # Study / Student FAQs
        ("study tips", "how to study"): 
        "Make a schedule, practice daily, and revise regularly 📚",

        ("cgpa", "gpa"): 
        "CGPA is the average of all your semester GPAs.",

        # Time & Date (static)
        ("date", "day"): 
        "I can’t check live date yet, but it’s a great day to learn something new 😊",

        ("thanks", "thankyou"):
        "You're welcome",

        # Exit
        ("bye", "exit", "quit"): 
        "Goodbye! Best of luck with your studies 👋"
    }

    for keywords, response in rules.items():
        for keyword in keywords:
            if keyword in user_input:
                return response

    return "Sorry, I don’t have an answer for that yet 🤔"


def chatbot():
    print("Chatbot: Hello! I am RuleBot. Ask me anything (type 'bye' to exit).")

    while True:
        user_input = input("You: ").lower()

        response = get_response(user_input)
        print("Chatbot:", response)

        if any(word in user_input for word in ["bye", "exit", "quit"]):
            break


chatbot()
