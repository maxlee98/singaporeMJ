from generateWalls import createWalls

class Game:
    def __init__(self):
        self.rounds = 1
        self.state = ['East', 'East']
        self.melds = self.special = {f"Player {i}": [] for i in range(1, 5)}

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

    



if __name__ == "__main__":
    game = Game()
    print(game.changeWind(['West', 'West']))
    round = game.startRound()
    # print(round)
    print(len(round['tiles']))
    hand = ['Bamboo-5', 'Dot-4', 'Red', 'East', 'Character-5', 'Character-6', 'West', 'Character-1', 'Bamboo-7', 'Bamboo-9', 'Dot-7', 'Character-9', 'White', 'F1', 'Cat']
    new_hand, new_tiles = game.replace_special_tiles("Player 1", hand, round['tiles'])
    print(game.special)
    print(new_hand)