#include <iostream>
#include <thread>
#include <chrono>

int fuelUsed  = 0;
int totalFuel = 1'000'000;

void engineBurn(const std::string& name)
{
    for (int i = 0; i < totalFuel; ++i)
    {
        fuelUsed++; // race condition
    }
    std::cout << name << " burn complete\n";
}

int main(void)
{
    std::thread t1(engineBurn, "Engine 1");
    std::thread t2(engineBurn, "Engine 2");

    t1.join();
    t2.join();

    // fuel used: 2000000
    // total fuel on board 1'000'000
    std::cout << "fuel used: " << fuelUsed << '\n';

    return EXIT_SUCCESS;
}