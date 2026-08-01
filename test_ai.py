from core.ai import AI

ai = AI()

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ai.ask(question)

    print("\nJarvis:", answer)