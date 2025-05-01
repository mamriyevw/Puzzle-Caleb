# Telegram Puzzle Bot Constructor

This is a simple template for creating your own puzzle bot using Telegram and Python.

## Features

- Load puzzles from JSON files
- Easy to configure messages
- Send images and questions
- Accept and check user answers

## How to Use

1. Clone the repo:
   ```
   git clone https://github.com/YOUR_USERNAME/telegram-puzzle-bot.git
   ```

2. Create a bot using [@BotFather](https://t.me/BotFather) and copy the token.

3. Add your token to Replit secrets or `.env`:
   ```
   API_TOKEN = your_token_here
   ```

4. Add your own puzzles inside `puzzles/` folder and images in `assets/`.

5. Run:
   ```
   python bot.py
   ```

## Example Puzzle

`puzzles/level1.json`:
```json
{
  "id": 1,
  "question": "What is shown in this image?",
  "image": "assets/puzzle1.jpg",
  "answer": "sun"
}
```