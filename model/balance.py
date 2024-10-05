class Balance(object):

    def __init__(self, current_balance: int):
        """
        Maintain balance as an object
        :param current_balance:
        """
        self.current_balance = current_balance

    def get_current_balance(self) -> int:
        """
        Gets current balance from class object
        :return: current balance on class
        :rtype int: balance as an integer
        """
        return self.current_balance