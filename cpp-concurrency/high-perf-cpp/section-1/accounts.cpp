#include <iostream>

class Account
{
    private:
        double m_balance;
    public:
        double getBalance();
        void deposit(double amount);
        void withdraw(double amount);
};