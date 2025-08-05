from app.openai_client import query_model

def main():
    print("🧠 OfficePall Assistant – ställ din fråga! (skriv 'exit' för att avsluta)\n")
    while True:
        user_input = input("💬 Du: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Avslutar. Tack för att du testade!")
            break
        response = query_model(user_input)
        print(f"\n🤖 OfficePall: {response}\n")

if __name__ == "__main__":
    main()