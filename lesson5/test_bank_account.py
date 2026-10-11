import unittest
from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Создание базового счёта перед каждым тестом (аналог фикстуры)."""
        self.account = BankAccount(owner="Алексей", account_number="AM123456", initial_balance=100.0)
        self.target_account = BankAccount(owner="Иван", account_number="AM654321", initial_balance=50.0)

    def test_initialization(self):
        """Проверка корректности создания счёта и начального баланса."""
        self.assertEqual(self.account.owner, "Алексей")
        self.assertEqual(self.account.account_number, "AM123456")
        self.assertEqual(self.account.balance, 100.0)

    def test_deposit_success(self):
        """Проверка успешного пополнения счёта."""
        new_balance = self.account.deposit(50.0)
        self.assertEqual(new_balance, 150.0)
        self.assertEqual(self.account.balance, 150.0)

    def test_deposit_negative_or_zero(self):
        """Негативный тест: пополнение отрицательной суммой или нулём."""
        with self.assertRaises(ValueError):
            self.account.deposit(-20.0)
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_success(self):
        """Проверка успешного снятия средств."""
        new_balance = self.account.withdraw(40.0)
        self.assertEqual(new_balance, 60.0)
        self.assertEqual(self.account.balance, 60.0)

    def test_withdraw_insufficient_funds(self):
        """Негативный тест: попытка снять сумму, превышающую баланс."""
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(200.0)
        # Убедимся, что баланс не изменился при ошибке
        self.assertEqual(self.account.balance, 100.0)

    def test_withdraw_negative(self):
        """Негативный тест: снятие отрицательной суммы."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-10.0)

    def test_transfer_success(self):
        """Проверка успешного перевода денег на другой счёт."""
        self.account.transfer(self.target_account, 30.0)
        # Баланс отправителя уменьшился, получателя — увеличился на ту же сумму
        self.assertEqual(self.account.balance, 70.0)
        self.assertEqual(self.target_account.balance, 80.0)

    def test_transfer_fail_keeps_state(self):
        """Проверка, что при невозможности перевода состояние счетов не меняется."""
        initial_sender_balance = self.account.balance
        initial_target_balance = self.target_account.balance

        with self.assertRaises(InsufficientFundsError):
            self.account.transfer(self.target_account, 500.0)

        # Состояния не должны измениться
        self.assertEqual(self.account.balance, initial_sender_balance)
        self.assertEqual(self.target_account.balance, initial_target_balance)

    def test_is_empty(self):
        """Проверка метода определения пустого счёта."""
        self.assertFalse(self.account.is_empty())  # Баланс 100
        
        self.account.withdraw(100.0)
        self.assertTrue(self.account.is_empty())   # Баланс стал 0


if __name__ == "__main__":
    unittest.main()