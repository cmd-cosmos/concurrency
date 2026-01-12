#include <iostream>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;

bool launch_auth = false;

void flightComputer()
{
    std::unique_lock<std::mutex> lock(mtx);

    std::cout << "flight computer awaiting laucnh configuration...\n";

    // release lock and sleep
    cv.wait(lock, [] { return launch_auth;});

    std::cout << "laucnh auth bit: true";
}

int main(void)
{
    std::thread t1(flightComputer);
    std::this_thread::sleep_for(std::chrono::seconds(2));

    {
        // while t1 sleeps --> mission control sets the launch auth bit to 1
        std::lock_guard<std::mutex> lock(mtx);
        launch_auth = true;
        std::cout << "\nmission control: set launchAuth bit = true\n\n";
    }

    cv.notify_one();
    t1.join();

    return EXIT_SUCCESS;
}