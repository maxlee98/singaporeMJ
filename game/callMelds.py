# 4. Functions to call for a meld

class Melds():
    def __init__(self):
        pass

    def can_form_chow(self, hand, discarded_tile):
        if '-' not in discarded_tile:
            return False
        number = int(discarded_tile.split('-')[1])
        suit = discarded_tile.split('-')[0]

        # Include the discarded tile in the hand before checking for a chow
        hand_with_discarded_tile = hand.copy()
        hand_with_discarded_tile.append(discarded_tile)

        for i in range(number - 2, number + 1):
            if i > 0 and i < 8:
                if f"{suit}-{i}" in hand_with_discarded_tile and f"{suit}-{i+1}" in hand_with_discarded_tile and f"{suit}-{i+2}" in hand_with_discarded_tile:
                    return True
        return False


    def can_form_pong(self, hand, discarded_tile):
        return hand.count(discarded_tile) >= 2

    def can_form_kong(self, hand, discarded_tile):
        return hand.count(discarded_tile) >= 3

    def can_meld(self, hand, discarded_tile):
        chow, pong, kong = False, False, False
        if self.can_form_chow(hand, discarded_tile):
            chow = True
        if self.can_form_pong(hand, discarded_tile):
            pong = True
        if self.can_form_kong(hand, discarded_tile):
            kong = True
        return chow, pong, kong
    

    def display_melds(self, hand, discarded_tile):
        chow, pong, kong = self.can_meld(hand, discarded_tile)
        action_space = {
            'chow': None,
            'pong' : None,
            'kong' : None
        }
        if chow:
            print("Can Chow")
            possible_chows = self.display_chow(hand, discarded_tile)
            action_space['chow'] = possible_chows
        if pong:
            possible_pong = self.display_pong(hand, discarded_tile)
            action_space['pong'] = possible_pong
        if kong:
            possible_kong = self.display_kong(hand, discarded_tile)
            action_space['kong'] = possible_kong

        return action_space

            
    
    def display_chow(self, hand, discarded_tile):
        tile_suit = discarded_tile.split('-')[0]
        tile_value = int(discarded_tile.split('-')[1])

        # Include the discarded tile in the hand before checking for a chow
        hand_with_discarded_tile = hand.copy()
        hand_with_discarded_tile.append(discarded_tile)

        possible_chows = []
        for i in range(-2, 1):  # Check for tile_value - 2, -1, 0
            chow_tiles = [f"{tile_suit}-{tile_value + j}" for j in range(i, i + 3)]
            if all(t in hand_with_discarded_tile for t in chow_tiles):
                possible_chows.append(chow_tiles)

        return possible_chows
    
    def display_pong(self, hand, discarded_tile):
        # Displaying the removed cards
        return [discarded_tile] * 2
    
    def display_kong(self, hand, discarded_tile):
        # Displaying the removed cards
        return [discarded_tile] * 3




if __name__ == "__main__":
    meld = Melds()
    hand = ['Bamboo-4', 'Dot-4', 'Red', 'East', 'Character-5', 'Character-6', 'West', 'Character-1', 'Bamboo-7', 'Bamboo-9', 'Bamboo-7', 'Character-9', 'White', 'Character-9', 'Bamboo-6']
    # print(meld.can_meld(hand, 'Character-9'))
    print(meld.display_melds(hand, 'Bamboo-5'))


