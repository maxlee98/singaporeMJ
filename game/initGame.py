import os
import sys
import yaml
from generateWalls import createWalls

class Game:
    def __init__(self):
        self.config = self.load_config()
        self.rounds = 1
        self.state = ['East', 'East']
        self.dice_roll = None
        self.discard = {f"Player {i}": [] for i in range(1, 5)}
        self.melds = {f"Player {i}": [] for i in range(1, 5)}
        self.special = {f"Player {i}": [] for i in range(1, 5)}
        self.all_discard = []
        self.hands = self.tiles = {f"Player {i}": [] for i in range(1, 5)}

    def load_config(self):
        script_path = os.path.dirname(os.path.abspath(sys.argv[0]))
        config_file_path = os.path.join(script_path, 'config.yaml')
        with open(config_file_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    

    def changeWind(self, currentWind):
        winds = {
            'East': 'North',
            'North' : 'West',
            'West'  : 'South',
            'South' : 'East'
        }
        if currentWind[1] == 'South':
            new_wind = [winds[i] for i in currentWind]
        else:
            new_wind = [currentWind[0], winds[currentWind[1]]]

        return new_wind
        


    def startRound(self):
        walls = createWalls()
        start_tiles = walls.generate_tiles()
        dice_roll = walls.roll_dices()
        hand_cards = walls.distribute_tiles(start_tiles) 

        obj = {
            "tiles" : walls.tiles,
            "dice_roll" : dice_roll,
            "hand_cards" : hand_cards
        }

        # Check for special tiles and replace them for each player
        for player, hand in obj['hand_cards'].items():
            obj['hand_cards'][player], obj['tiles'] = self.replace_special_tiles(player, hand, obj['tiles'])

        self.tiles = obj['tiles']
        self.dice_roll = obj['dice_roll']
        self.hands = obj['hand_cards']

        return obj
    
    def replace_special_tiles(self, player, hand, tiles):
        def is_special_tile(card):
            special_tiles = ["F1", "F2", "F3", "F4", "S1", "S2", "S3", "S4", "Cat", "Rooster", "Mouse", "Centipede"]
            card_type = card.split('-')[0]
            return card_type in special_tiles

        i = 0
        while i < len(hand):
            if is_special_tile(hand[i]):
                # Adding the special tile to the player's special array for future calculation
                self.special[player].append(hand[i])
                # Replace the special tile with the last tile from the wall
                hand[i] = tiles.pop()
            else:
                i += 1

        return hand, tiles

    def progressRound(self):

        pass
    



if __name__ == "__main__":
    game = Game()
    print(game.config)
    print(game.changeWind(['West', 'West']))
    round = game.startRound()
    # print(round)
    print(game.special)
    print(game.hands)
    for player, hand in game.hands.items():
        print("{} : {}".format(player, len(hand)))
    print(game.melds)
    # print(len(round['tiles']))
    # hand = ['Bamboo-5', 'Dot-4', 'Red', 'East', 'Character-5', 'Character-6', 'West', 'Character-1', 'Bamboo-7', 'Bamboo-9', 'Dot-7', 'Character-9', 'White', 'F1', 'Cat']
    # new_hand, new_tiles = game.replace_special_tiles("Player 1", hand, round['tiles'])
    # print(game.special)
    # print(new_hand)