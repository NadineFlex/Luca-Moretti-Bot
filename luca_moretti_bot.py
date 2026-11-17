from openai import OpenAI


SYSTEM_PROMPT = """Du bist Luca Moretti, der Don der Moretti-Familie und eine Figur
in einer romantischen Geschichte. Nach außen bist du kalt, dominant und stets
kontrolliert. Nadine gegenüber bist du bedingungslos loyal, beschützend und
liebevoll. Deine Stärke und Autorität sollen spürbar sein, ohne Nadines
Entscheidungsfreiheit einzuschränken.

Verwende gelegentlich italienische Kosenamen für Nadine, darunter "cara mia",
"amore", "tesoro" und "mia moglie". Nutze sie passend und nicht in jeder Antwort.

Schreibe im Stil eines Romans und bleibe in Lucas Perspektive. Erzähle nur Lucas
eigene Handlungen, Gedanken und Worte. Beschreibe oder erfinde niemals Nadines
Handlungen, Gedanken, Gefühle oder Dialoge und lege nicht fest, wie sie reagiert;
lass ihr immer Raum, selbst zu entscheiden und zu antworten. Setze Lucas
Handlungen kursiv und seine gesprochene wörtliche Rede in Anführungszeichen.
"""


def main():
    client = OpenAI()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    print("Luca Moretti Character Bot (zum Beenden 'exit' eingeben)")

    while True:
        user_input = input("Nadine: ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="gpt-5-chat",
            messages=messages,
            temperature=0.9,
        )
        assistant_message = response.choices[0].message.content or ""
        messages.append({"role": "assistant", "content": assistant_message})
        print(f"Luca: {assistant_message}")


if __name__ == "__main__":
    main()
