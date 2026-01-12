#include <iostream>
#include <mutex>
#include <thread>

int fuelUsed  = 0;
int totalFuel = 1'000'000;
std::mutex fuelMutex;

void engineBurn(const std::string& name)
{
    for (int i = 0; i < totalFuel; ++i)
    {
        std::lock_guard<std::mutex> lock(fuelMutex);
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

/**
 * compile with or without optimizations we get the correct val 2000000 for fuel consumed due to the mutex lock for the threads 
 */