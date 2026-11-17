# Luca Moretti Character Bot

A small command-line roleplay bot featuring Luca Moretti.

## Requirements

- Python 3.9 or newer
- An OpenAI API key

## Setup

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Set `OPENAI_API_KEY` in your environment. In PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-api-key"
```

On macOS or Linux:

```bash
export OPENAI_API_KEY="your-api-key"
```

Keep your API key private; do not add it to the source files or commit it.

## Start

```bash
python luca_moretti_bot.py
```

Enter Nadine's messages at the prompt. Type `exit` to end the conversation.
