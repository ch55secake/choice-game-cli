from typing import Annotated

import typer

from model.balance import Balance
from model.inventory import Inventory
from state.game_state import GameState

app = typer.Typer()

skipped_option = typer.Option(parser=lambda _: _, hidden=True, expose_value=False)

@app.command("state")
def state(existing_game_state: Annotated[GameState, skipped_option] = "blalalsala"):
    GameState.view_current_state(existing_game_state)

@app.command("init")
def init():
    inventory: Inventory = Inventory()
    balance: Balance = Balance()
    game_state: GameState = GameState(inventory=inventory, balance=balance)
    GameState.view_current_state(game_state)

@app.callback()
def callback():
    """
    Choice game, rewritten into CLI.
    """

if __name__ == '__main__':
    app()