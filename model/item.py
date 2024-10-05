from rich import print_json, json


class Item(object):
    """
    Class representation of item object
    """
    def __init__(self, value: int, desc: str, name: str):
        self.value = value
        self.desc = desc
        self.name = name

    def get_item_list(self) -> list[str]:
        """
        Get item as a list
        :return: item as list
        """
        return [self.value, self.desc, self.name]

    def get_item_dict(self) -> dict[str, dict[str, int]]:
        """
        Get item as a dictionary
        :rtype: dict[str, dict[str, int]]
        :return: item as a dict
        """
        return {self.name: {self.desc, self.value}}

    def get_item_json(self) -> json:
        """
        Get item as json so rich can pretty print it
        :return: json object of item
        """
        return json.loads(self.get_item_dict().__str__())

    def __str__(self):
        """
        Pretty print item as json
        """
        print_json(self.get_item_json())
