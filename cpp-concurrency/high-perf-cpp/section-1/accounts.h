#include <iostream>

class Account
{
    private:
        double m_balance;
    public:
        Account( double balance);
        double getBalance();
        void deposit(double amount);
        void withdraw(double amount);
};