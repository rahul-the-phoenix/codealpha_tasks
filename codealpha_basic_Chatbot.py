import datetime

def chatbot():

    print("Simple Chatbot 🤖")
    name = input("Bot: What is your name? ")

    print("Bot: Hello", name + "! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a simple chatbot.")

        elif user == "time":
            now = datetime.datetime.now()
            print("Bot: Current time is", now.strftime("%H:%M"))

        elif user == "date":
            today = datetime.date.today()
            print("Bot: Today's date is", today)

        elif user == "thanks":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye", name + "!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()