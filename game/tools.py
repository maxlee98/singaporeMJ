class tools:
    def __init__(self):
        pass

    def sort_hand(self, hand):
        def card_priority(card):
            priority = {
                "Character": 1,
                "Dot": 2,
                "Bamboo": 3,
                "East": 4, "South": 4, "West": 4, "North": 4,
                "Red": 4, "Green": 4, "White": 4,
                "F1": 5, "F2": 5, "F3": 5, "F4": 5,
                "S1": 6, "S2": 6, "S3": 6, "S4": 6,
                "Cat": 7, "Rooster": 7, "Mouse": 7, "Centipede": 7
            }
            card_type = card.split('-')[0]
            return priority[card_type]

        hand = sorted(hand, key=lambda x: (card_priority(x), x))
        return hand
    







if __name__ == "__main__":
    example_hand = ['Dot-8', 'South', 'Centipede', 'South', 'Character-7', 'Bamboo-7', 'Dot-8', 'Character-4', 'S3', 'Green', 'Dot-1', 'Dot-4', 'East']
    tool = tools()
    print(tool.sort_hand(example_hand))