from model.board import Board, FixedBoardFactory
from model.player import Player
from model.gamestate import GameState
from controller.controller import GameController


def main():

    tiles = FixedBoardFactory.create_tiles()
    board = Board(tiles)

    players = [
        Player([], 0),
        Player([], 0),
        Player([], 0),
        Player([], 0)
    ]

    state = GameState(board=board, players=players)

    controller = GameController(state)

    controller.run(max_turns=10)


if __name__ == "__main__":
    main()