# main.py

from logs.assistant import run_assistant

if __name__ == "__main__":
    print("🤖 Smart Support Bot running. Type 'exit' to quit.\n")
    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = run_assistant(user_input)
        print("Bot:", response)
