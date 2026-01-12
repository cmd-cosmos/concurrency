#include <iostream>
#include <thread>
#include <atomic>

std::atomic<int> fuelUsed{0};

void engineBurn(const std::string& name)
{
    for (int i = 0; i < 1'000'000; ++i)
    {
        fuelUsed++;
    }
    std::cout << name << " burn complete\n";
}

int main(void)
{
    std::thread t1(engineBurn, "Engine 1");
    std::thread t2(engineBurn, "Engine 2");

    t1.join();
    t2.join();

    std::cout << "fuel used: " << fuelUsed << '\n';

    return EXIT_SUCCESS;
}