from __future__ import annotations

from time import sleep
from hashlib import sha256

class Card:

    @staticmethod
    def get_value_dict():
        valueDict: dict = {f"{i + 1}": i + 1 for i in range(9)}
        valueDict["T"] = 10
        valueDict["J"] = 11
        valueDict["Q"] = 12
        valueDict["K"] = 13
        return valueDict.copy()

    @staticmethod
    def get_suit_dict():
        # CHaSeD order
        suitDict: dict = {"C": 4, "H": 3, "S": 2, "D": 1}
        return suitDict.copy()

    @staticmethod
    def str_2_card(card: str) -> Card:
        if len(card) == 2:
            if card[0] not in Card.get_value_dict():
                raise Exception(
                    "A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")
            if card[1] not in Card.get_suit_dict():
                raise Exception(
                    "A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")
            return Card(Card.get_value_dict()[card[0]], Card.get_suit_dict()[card[1]])

        if len(card) != 3:
            raise Exception("A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")
        if card[0] not in Card.get_value_dict():
            raise Exception("A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")
        if card[1] != " ":
            raise Exception("A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")
        if card[2] not in Card.get_suit_dict():
            raise Exception("A card doesn't much the pattern (Number + Suit e.g Ten Of Spades: T S, Four Of Diamonds 4 D)")

        return Card(Card.get_value_dict()[card[0]], Card.get_suit_dict()[card[2]])


    def __init__(self, value: int, suit: int):
        assert 1 <= value <= 13
        assert 1 <= suit <= 4

        self.value = value
        self.suit = suit

    @staticmethod
    def switch_k_v(d: dict):
        return {y: x for x, y in d.items()}

    def __str__(self):
        return f"{Card.switch_k_v(Card.get_value_dict())[self.value]} {Card.switch_k_v(Card.get_suit_dict())[self.suit]}"

    def __lt__(self, other: Card):
        if self.value != other.value: return self.value < other.value
        sValue = self.value * self.suit
        oValue = other.value * other.suit
        return sValue < oValue

    def __hash__(self):
        return int(sha256(f"{self}".encode()).hexdigest(), 16)


def main():
    # Values will be in Chased order
    addValueDict: dict = {123: 1, 132: 2, 213: 3, 231: 4, 312: 5, 321: 6}
    cards: list[Card] = [Card.str_2_card(input(f"Card name and suit (Four Of Diamonds: 4 D, Ace is 1) {i + 1}: ").upper()) for i in range(4)]

    # Checks if the pattern is correct
    if len(set(cards)) != 4:
        print("A card or more are duplicates")
        exit()

    card1 = cards.pop(0)

    predicted_suit = card1.suit

    cards.reverse()

    sorted_cards3 = sorted(cards)

    sortedCardDict = {sorted_cards3[i]: f"{i + 1}" for i in range(3)}

    addition_number = int("".join([sortedCardDict[cards[i]] for i in range(3)]))

    predicted_value = (card1.value + addValueDict[addition_number]) % 13
    if predicted_value == 0: predicted_value = 13

    predicted_card = Card(predicted_value, predicted_suit)

    print("\n\n\n\nReading Mind...")

    sleep(2)

    print(f"\n\n\n\n{predicted_card}")






if __name__ == '__main__':

    main()






