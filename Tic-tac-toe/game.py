'''This module contains class Game which implements
simple variant of tic-tac-toe'''


class Game:
    '''Simple tic-tac-toe console game.'''

    def __init__(self):
        self.board = list(range(1, 10))
        self.count_moves = 0
        self.symbols = ('X', 'O')

    def print_board(self):
        '''Function for printing table in pretty format.'''

        print('-------------')
        for line in range(3):
            print(f'| {self.board[3 * line]} |', end='')
            print(f' {self.board[3 * line + 1]} |', end='')
            print(f' {self.board[3 * line + 2]} |')
        print('-------------')

    def make_move(self, response):
        '''Validating user\'s input. Returns True if everything is correct.'''

        error_message = 'You need to write integer from 1 to 9'

        if not response.isdigit() or response[0] == '0':
            print(error_message)
            return False

        move = int(response)
        if not 1 <= move <= 9:
            print(error_message)
            return False

        if self.board[move - 1] in self.symbols:
            print('This place is taken')
            return False

        self.board[move - 1] = self.symbols[self.count_moves % 2]
        self.count_moves += 1
        return True

    def request_move(self):
        '''Taking input from the user.'''

        got_move = False
        while not got_move:
            self.print_board()
            response = input('Your move(number from 1 to 9): ')
            got_move = self.make_move(response)

    def check_win(self):
        '''Finds lines with same character.'''

        # checking horizontal lines
        for line in range(3):
            if len(set(self.board[3 * line:3 * line + 3])) == 1:
                return True

        # checking vertical lines
        for line in range(3):
            if len(set(self.board[line::3])) == 1:
                return True

        # checking diagonales
        if len(set(self.board[0::4])) == 1 or len(
                set(self.board[2:8:2])) == 1:
            return True

        return False

    def run(self):
        '''Starts game.'''

        has_winner = False
        while self.count_moves < 9 and not has_winner:
            self.request_move()
            has_winner = self.check_win()

        self.print_board()

        if has_winner:
            winner = self.symbols[(self.count_moves + 1) % 2]
            print(f'{winner} won!')
        else:
            print("It's draw!")


if __name__ == '__main__':
    Game().run()
