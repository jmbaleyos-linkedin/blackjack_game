# blackjack_game
Blackjack Game in Python

This is a Blackjack game built in Python as part of my journey through learning Python.

It’s my first full project after one week of learning Python, applying fundamental concepts like dictionaries, loops, conditionals, and functions. To make the game more engaging, I also integrated ASCII art for cards.

Features:
* Card dealing system
    - Cards are drawn randomly with proper removal (no duplicates).
* Dynamic scoring system
    - Handles Ace values (1 or 11 depending on hand total).
* Player functionality
    - Choose to hit (get another card) or stand (end turn).
* Dealer AI
    - Dealer automatically draws until reaching 16 or higher.
* Game outcomes
    - Detects win, lose, or draw conditions based on final totals.
* Deck reset
    - Deck reshuffles automatically when running low on cards.
* ASCII card display
    - Cards are printed with ASCII art and shown side by side for readability.

Technologies Used:
* Python 3
* Built-in libraries: random
* Custom ASCII art for card representation

📁 blackjack-game
│── main.py         # Main game logic
│── art.py          # ASCII art for cards and logo
│── README.md       # Project documentation

🚀 Getting Started
1. Clone the repository
    git clone https://github.com/<your-username>/blackjack-game.git
    cd blackjack-game
2. Run the game
    python main.py

📸 Sample Gameplay
Do you want to play a game of Blackjack? Type 'y' or 'n': y

🂡  Blackjack Game!  🃏

<pre>
Player’s cards:
┌───────┐ ┌───────┐
│A      │ │K      │
│       │ │       │
│   ♠   │ │   ♦   │
│       │ │       │
│      A│ │      K│
└───────┘ └───────┘
Score 21.

Dealer’s cards:
┌───────┐
│8      │
│       │
│   ♥   │
│       │
│      8│
└───────┘
Score 8.
</pre>
📌 Future Improvements:
    - Add betting system and chip management
    - Allow multiple players
    - Improve dealer AI strategy
    - Add GUI version with Tkinter or PyGame
