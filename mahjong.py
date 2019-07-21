from random import shuffle
from enum import Enum

class Type(Enum):
    bamboo = 0
    dot = 1
    character = 2
    wind = 3
    dragon = 4
    season = 5
    flower = 6

class Dragon(Enum):
    red = 0
    green = 1
    blue = 2

class Wind(Enum):
    east = 1
    south = 2
    west = 3
    north = 4

class Tile:
    def __init__(self, type, value):
        self.type = type
        self.value = value
       
class Player:
    def __init__(self):
        self.hand = []
        self.revealed = []
        
    def has(self, type, value):
        for tile in hand:
            if tile.type.value == type:
                pass
        
class Round:
    def __init__(self):
        self.stack = []
        for n in range(4):
            for i in range(1,10):
                for j in range(3):
                    self.stack.append(Tile(j, i))
            for i in range(4):
                self.stack.append(Tile(3, i))
            for i in range(3):
                self.stack.append(Tile(4, i))
        for i in range(1,5):
            for j in range(5, 7):
                self.stack.append(Tile(j, i))
        shuffle(self.stack)
        self.pile = []
        self.discard = None
        
    def deal(self):
        self.east = Player()
        self.south = Player()
        self.west = Player()
        self.north = Player()
        for m in range(3):
            for i in self.east, self.south, self.west, self.north:
                for n in range(4):
                    i.hand.append(self.pick())
        for i in self.east, self.south, self.west, self.north:
            i.hand.append(self.pick())
        self.east.hand.append(self.pick())
    
    def deal_flowers(self):
        any = False
        for i in self.east, self.south, self.west, self.north:
            counter = 0
            copy = i.hand.copy()
            for j in range(len(copy)):
                if copy[j].type == 5 or copy[j].type == 6:
                    counter += 1
                    any = True
                    i.revealed.append(i.hand.pop(j))
            for j in range(counter):
                i.hand.append(self.pick_flower())
        if any:
            self.deal_flowers()
                    
    def crack(self, roll):
        start = ((roll%4-1)*36 + 2*roll)%144
        self.stack = self.stack[start:] + self.stack[:start]
        return start
    
    def __pick_flower(self):
        tile = self.stack[len(self.stack)-1]
        self.stack = self.stack[:len(self.stack)-1]
        return tile
    
    def __pick(self):
        tile = self.stack[0]
        self.stack = self.stack[1:]
        return tile
    
    def discard(self, seat, tile):
        player = self.__get_player(seat)
        self.discard = player.hand.pop(tile)
        self.pile.append(self.discard)
    
    def draw(self, seat):
        player = self.__get_player(seat)
        tile = self.__pick()
        player.hand.append(tile)
        return tile
    
    def draw_flower(self, seat):
        player = self.__get_player(seat)
        tile = self.__pick_flower()
        player.hand.append(tile)
        return tile
    
    def reveal(self, seat, tiles):
        player = self.__get_player(seat)
        shown = []
        for i in tiles.sort(reverse=True):
            player.revealed.append(player.hand[i])
            shown.append(player.hand[i])
            del player.hand[i]
        return shown
    
    def steal(self, seat):
        player = self.__get_player(seat)
        self.pile.pop(len(self.pile)-1)
        player.hand.append(self.discard)
        tile = self.discard
        self.discard = None
        return tile
    
    def __get_player(self, wind):
        if seat == Wind.east:
            return self.east
        elif seat == Wind.south:
            return self.south
        elif seat == Wind.west:
            return self.west
        elif seat == Wind.north:
            return self.north
    
    def print_stack(self):
        for tile in self.stack:
            if tile.type==4:
                print(Type(tile.type), Dragon(tile.value))
            elif tile.type==3:
                print(Type(tile.type), Wind(tile.value))
            else:
                print(Type(tile.type), tile.value)
                
    def print_player_hands(self):
        for i in (self.east, 'East'), (self.south, 'South'), (self.west, 'West'), (self.north, 'North'):
            print(i[1])
            for tile in i[0].hand:
                if tile.type==4:
                    print(Type(tile.type), Dragon(tile.value))
                elif tile.type==3:
                    print(Type(tile.type), Wind(tile.value))
                else:
                    print(Type(tile.type), tile.value)
            print()
            for tile in i[0].revealed:
                if tile.type==4:
                    print(Type(tile.type), Dragon(tile.value))
                elif tile.type==3:
                    print(Type(tile.type), Wind(tile.value))
                else:
                    print(Type(tile.type), tile.value)
            print()                