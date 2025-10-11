#include <iostream>
#include <thread>
#include <mutex>
#include "accounts.h"

enum ThreadType{
    DEPOSITOR_THREAD,
    WITHDRAWER_THREAD
};

std::mutex locker;

Account account(100000.00); // initialize an account