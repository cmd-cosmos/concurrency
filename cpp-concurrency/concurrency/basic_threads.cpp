#include <iostream>
#include <thread>
#include <chrono>

void subsystemCheck(const char* name) {
    std::cout << "\nChecking subsys: " << name << "\n";
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
}

int main(void)
{
    std::thread t1(subsystemCheck, "Navigation");
    std::thread t2(subsystemCheck, "GNC");
    std::thread t3(subsystemCheck, "Propulsion");
    std::thread t4(subsystemCheck, "Electronics");
    std::thread t5(subsystemCheck, "Payload");
    std::thread t6(subsystemCheck, "Structures");

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();
    t6.join();

    std::cout << "\nAll subsystems checked\n";

    return EXIT_SUCCESS;
}