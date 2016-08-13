class Game():

    def __init__(self, show_each_turn=True):
        self._players = ["X", "0"]
        self._each_turn = show_each_turn
        # TODO: think of a better method to find the winner
        # than searching through a list each turn
        self.winning_positions = [
            [[0,0], [0,1], [0,2]],
            [[1,0], [1,1], [1,2]],
            [[2,0], [2,1], [2,2]],
            [[0,0], [1,0], [2,0]],
            [[0,1], [1,1], [2,1]],
            [[0,2], [1,2], [2,2]],
            [[0,0], [1,1], [2,2]],
            [[2,0], [1,1], [0,2]]
            ]
        # create an empty grid
        self.grid = [["·"]*3 for i in range(3)]
        # list of current player positions
        self.cross_pos = []
        self.nought_pos = []
        self.winner = None
        self.last_player = None


    def __len__(self):
        """ number of moves played """
        return len(self.cross_pos) + len(self.nought_pos)


    def reset(self):
        """ reset grid and player moves """
        self.grid = [["·"]*3 for i in range(3)]
        self.cross_pos = []
        self.nought_pos = []
        self.winner = None
        self.last_player = None


    def show_grid(self):
        """ print out the grid in simple format """
        for i in self.grid:
            print(*i, "\n")
        print("\n")
        # TODO better grid ouput


    def place(self, player, position):
        """ place item on board in given position """

        if player not in self._players:
            raise ValueError("invalid player, options are 'X' or '0'")

        if self.last_player == player:
            raise ValueError("it's the other player's turn!")

        # check there is not already an item in that position
        if self.grid[position[0]][position[1]] == "·":
            self.grid[position[0]][position[1]] = player
        else:
            raise IndexError("already an item at that position")

        # update player position list
        if player == "X":
            self.cross_pos.append(position)
        elif player == "0":
            self.nought_pos.append(position)

        if self._each_turn:
            self.show_grid()

        self.last_player = player
        self.check_for_winner(player)


    def check_for_winner(self, player):
        """
        check the grid to see if there are any winners
        if so, return name of winning player
        """
        # if a player has already won, don't set new winner
        if self.winner != None:
            return None

        # determine positions of player
        if player == "X":
            positions = self.cross_pos
        if player == "0":
            positions = self.nought_pos

        for winning_moves in self.winning_positions:
            total = 0
            for winning_pos in winning_moves:
                if winning_pos in positions:
                    total+=1
                if total == 3:
                    self.winner = player
                    print("~~~ {} wins! ~~~".format(self.winner))
