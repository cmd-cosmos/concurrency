#include <iostream>
#include <thread>
#include <chrono>

void groundSysInspection()
{
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    std::cout << "ground system inspections complete\n";
}

int main(void)
{
    std::cout << "Main thread: GSE checks initiated\n";

    std::thread t1(groundSysInspection);

    // in case the daughter thread is not joined --> std::terminate
    //  Main thread: GSE checks initiated
    //  Main thread: ground checks complete
    //  terminate called without an active exception
    // t1.join();

    std::cout << "Main thread: ground checks complete\n";

    return EXIT_SUCCESS;
}
