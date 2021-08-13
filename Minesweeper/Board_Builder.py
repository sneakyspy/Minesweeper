from Minesweeper.State import TileState, GameState

def board_builder(row_count, column_count):
    grid = []
    for row_number in range(0, row_count):
        grid.insert(row_number, [])
        for column_number in range(0, column_count):
            tile = TileState.NUMBER
            grid[row_number].insert(column_number, tile)
    state = GameState(grid, False)
    state.generate_bomb()
    return state