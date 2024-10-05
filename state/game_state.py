from datetime import datetime

from model.balance import Balance
from model.inventory import Inventory


class GameState(object):

    def __init__(self, updated_at: datetime, inventory: Inventory, balance: Balance):
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







