from model import item
from model.item import Item
from rich import print


class Inventory(object):

    def __init__(self):
        """
        Maintains list of items that user has on them
        """
        self.inv: list[item] = []

    def __str__(self):
        return self.get_string_items()

    def add_to_inv(self, new_item: Item) -> None:
        """
        Appends item to current inventory
        """
        self.inv.append(new_item)

    def has_item(self, current_item: item) -> bool:
        """
        Check if inventory currently contains item
        :return: bool based on whether item is present
        """
        for owned_item in iter(self.inv):
            if owned_item is current_item:
                return True
            else:
                return False

    def remove_item(self, current_item: item) -> None:
        """
        Removes the current item from the inventory as long as user doesn't currently have the item
        :param current_item: item intended for removal
        :return: None or prints message saying item was not removed
        """
        if self.has_item(current_item=current_item):
            self.inv.remove(current_item)
        else:
            print("[bold red]Cannot remove item from inventory as it is not owned![/bold red]")

    def get_string_items(self) -> str:
        """
        Get all items in inventory as strings, unless empty then return string that represents empty
        :return: string representation of items
        """
        for value in iter(self.inv):
            if len(self.inv) == 0:
                return "[bold red]poo![/bold red]"
            else:
                ", ".join(value)
