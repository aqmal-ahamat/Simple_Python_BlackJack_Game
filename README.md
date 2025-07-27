# 🃏 Blackjack Game (Python)

A simple command-line Blackjack game written in Python. This project is part of my portfolio to demonstrate core Python skills including loops, functions, control flow, and basic game logic.

---

## 🃏 Game Rules

- Both the player (you) and the dealer (computer) are dealt 2 cards.

- You can see both of your cards and only one of the dealer’s cards.

- You may choose to:

  - Hit – draw another card.

  - Stand – stop drawing cards.

- If your total exceeds 21, you bust and lose immediately.

- After you stand, the dealer reveals their hidden card.

- The dealer must draw cards until their total is 17 or higher.

- If the dealer’s total exceeds 21, they bust and you win.

- If neither player busts, the hand with the higher total wins.

- If both totals are the same, it results in a draw (also called a "push").

- Card values:

  - 2–10: Face value

  - J, Q, K: 10 points each

  - Ace (A): 1 or 11 points — whichever is more favorable without busting

<br>

---


## 🎮 Features

- Player vs. Dealer gameplay
- Standard Blackjack rules (21-point system)
- Random card dealing with score updates
- Smart Ace logic: counts as 11 or 1 based on hand
- Dealer auto-draws until reaching 17 or higher
- Option to replay after each game
<br>

---


## 📦 Requirements

- Python 3.x
- No external libraries needed
<br>

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/aqmalahamat/blackjack-game.git
   ```
2. Navigate into the project folder:  
   ```bash
   cd blackjack-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```
<br>

---

## ✍🏻 What I Learned

✅ Core Python Programming
Used variables, functions, conditionals, loops, and data structures (lists) to implement game logic.

✅ Randomization
Utilized the random module to simulate realistic card draws.

✅ Game Flow Logic
Designed a turn-based system where both the player and dealer take actions based on Blackjack rules.

✅ Custom Scoring System
Implemented a dynamic card value system, including correct handling of Aces as 1 or 11 depending on the situation.

✅ User Interaction via Console
Handled user input to guide gameplay and created a clear, interactive console experience.

✅ Basic User Input Validation
Validated player responses (e.g., 'y' or 'n') to prevent unexpected behavior and maintain a smooth game flow.

✅ Control Flow & State Management
Managed game state using flags and loops to allow replayability and structured progression.

✅ Basic Problem Solving
Translated real-world Blackjack rules into logical, functional Python code.

<br>

---


