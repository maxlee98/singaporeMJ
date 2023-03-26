import random

class createWalls:
    def __init__(self) -> None:
        self.tiles = self.generate_tiles()
        self.diceRoll = self.roll_dices()

    # 1. Functions for generating the wall cards
    def generate_tiles(self):
        suits = ['Bamboo', 'Character', 'Dot']
        honors = ['East', 'South', 'West', 'North', 'Red', 'Green', 'White']
        flowers = ['F1', 'F2', 'F3', 'F4']
        seasons = ['S1', 'S2', 'S3', 'S4']
        animals = ['Cat', 'Rooster', 'Mouse', 'Centipede']
        tiles = []

        for suit in suits:
            for number in range(1, 10):
                tiles.extend([f"{suit}-{number}"] * 4)

        for honor in honors:
            tiles.extend([honor] * 4)

        for flower in flowers:
            tiles.extend([flower])

        for season in seasons:
            tiles.extend([season])

        for animal in animals:
            tiles.extend([animal])

        random.shuffle(tiles)
        return tiles

    # 2. Functions that rolls 3 dices
    # Function might not be needed, given dice roll just adds another layer of random. Random already present in wall building
    def roll_dices(self):
        return [random.randint(1, 6) for _ in range(3)]

    # 3. Distribute wall tiles to the different players
    def distribute_tiles(self, tiles):
        players = {f"Player {i}": [] for i in range(1, 5)}

        # Each player takes 4 cards at a time until they reach 12 cards
        for i in range(3):
            for j in range(4):
                player = f"Player {j + 1}"
                players[player].extend(tiles[:4])
                tiles = tiles[4:]


        # First player takes 2 cards, the next card, then skips 3 cards and takes the 5th card
        last_cards = tiles[:6]
        tiles = tiles[6:]
        players["Player 1"].append(last_cards.pop(4)) # 5th card
        players["Player 1"].append(last_cards.pop(0)) # Popped the first card

        # Other players take their respective cards
        players["Player 2"].append(last_cards.pop(0))
        players["Player 3"].append(last_cards.pop(0))
        players["Player 4"].append(last_cards.pop(0))
        self.tiles = tiles
    
        return players





if __name__ == "__main__":
    game = createWalls()
    tiles = game.tiles
    hands = game.distribute_tiles(tiles)
    # print(hands)
    for player,hand in hands.items():
        print("{} cards, {} : {}".format(len(hand), player, hand))
    # print(game.diceRoll)
    # print(len(tiles))
    # print(tiles)
