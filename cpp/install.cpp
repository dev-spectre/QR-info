#include <iostream>    

int main(){

    std::system("python -m pip install --upgrade pip");
    std::system("pip install -r .\\requirements.txt ");

    return 0;
}