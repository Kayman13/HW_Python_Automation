
import random
from typing import List


class Card:
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                   'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number: str, mast: str):
        self.number = number
        self.mast = mast

    def __str__(self) -> str:
        if self.mast == "Joker":
            return f"Joker {self.number}"
        return f"{self.mast} {self.number}"


class CardsDeck:
    def __init__(self):
        self.cards: List[Card] = []
        self._generate_deck()

    def _generate_deck(self):
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))

        self.cards.append(Card("Black", "Joker"))
        self.cards.append(Card("Red", "Joker"))

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self, index: int) -> Card:
        if not 1 <= index <= len(self.cards):
            raise ValueError("Card number must be between 1 and 54")
        return self.cards[index - 1]


if __name__ == "__main__":
    deck = CardsDeck()
    deck.shuffle()

    card_number = int(input('Выберите карту из колоды в 54 карт: '))
    card = deck.get(card_number)
    print(f'Your card is: {card}')

    card_number = int(input('Выберите карту из колоды в 54 карт: '))
    card = deck.get(card_number)
    print(f'Your card is: {card}')
