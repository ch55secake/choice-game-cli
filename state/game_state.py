import json

from rich import print
from datetime import datetime
from model.balance import Balance
from model.inventory import Inventory


class GameState(object):

    def __init__(self,  inventory: Inventory, balance: Balance, updated_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        """
        Represent current game state which will be transformed into json and written to a file
        :param updated_at: last time users inventory was updated
        :param inventory: list of maintained items
        :param balance: balance represented as int
        """
        self.updated_at = updated_at
        self.inventory = inventory
        self.balance = balance

    def get_updated_at(self) -> datetime:
        """
        Gets updated at from the current game state
        :returns: updated at from the current game state
        :rtype datetime:
        """
        return self.updated_at

    def get_inventory(self) -> Inventory:
        """
        Gets current inventory from the current game state
        :return: inventory from the current game state
        :rtype Inventory:
        """
        return self.inventory

    def get_balance(self) -> Balance:
        """
        Gets the balance from the current game state, further interaction can be done via the object
        :return: balance from the current game state
        :rtype Balance:
        """
        return self.balance

    def view_current_state(self):
        print(f"[bold green]:money_with_wings: Current balance is: {self.get_balance().get_current_balance()}![/bold green]\n"
              f"[bold]:open_file_folder: Current state of inventory: {self.inventory.__str__()}![/bold]\n"
              f"[bold]State last updated at: {self.get_updated_at()}![/bold]\n")

class StateManager(object):

    def __init__(self, state: GameState):
        """
        Manage the current game state update inventory, load new state, update existing state, destroy state
        :param state: current game state
        """
        self.state = state

    @staticmethod
    def update_state(existing_game_state: GameState, new_balance: Balance = None, new_inventory: Inventory = None) -> GameState:
        """
        Update the current game state will only update values provided, will always update timestamp
        on the GameState
        :param existing_game_state: current game state
        :param new_balance: balance if provided, if not provided will be none
        :param new_inventory: inventory if provided, if not provided will be none
        :return: new game state
        """
        current_time = datetime.now()
        game_state = GameState(updated_at=current_time, inventory=GameState.get_inventory(self=existing_game_state), balance=GameState.get_balance(self=existing_game_state))
        arguments = {arg: locals()[arg] for arg in ('new_balance', 'new_inventory')}
        for key, value in arguments.iteritems():
            setattr(game_state, key, value)

        return game_state

    def read_state(self) -> GameState:
        """
        Reads the current state from a file
        :return: the state that was read from json file
        """
        with open("~/static/state.json", "r") as f:
            current_state = json.load(f)
            new_state: GameState = GameState(inventory=current_state["inventory"], balance=current_state["balance"], updated_at=current_state["updatedAt"])
            self.state = new_state
        return self.state

    








