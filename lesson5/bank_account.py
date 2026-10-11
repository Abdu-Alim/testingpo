class InsufficientFundsError(Exception):
    """Исключение при нехватке средств на счету."""
    pass


class BankAccount:
    def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Имя владельца должно быть строкой.")
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Номер счёта должен быть строкой.")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")

        self._owner = owner
        self._account_number = account_number
        self._balance = float(initial_balance)

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        """Пополнение счёта."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма пополнения должна быть числом.")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        
        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Снятие денежных средств со счёта."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма снятия должна быть числом.")
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть больше нуля.")
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств на счету.")

        self._balance -= float(amount)
        return self._balance

    def transfer(self, target_account, amount: float) -> None:
        """Перевод денежных средств на другой счёт."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма перевода должна быть числом.")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть больше нуля.")
        
        # Если снять не получится (выбросится ошибка), балансы останутся неизменными
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств для перевода.")

        # Выполняем транзакцию
        self.withdraw(amount)
        target_account.deposit(amount)

    def is_empty(self) -> bool:
        """Определяет, является ли счёт пустым (баланс равен нулю)."""
        return self._balance == 0.0