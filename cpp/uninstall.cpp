#include <iostream>
#include <filesystem>
#include <cstring>

int main(){

    std::filesystem::path dir_path = std::filesystem::current_path();
    std::string cwd_str = dir_path.generic_string();
    char* cwd = new char[cwd_str.length() + 1];
    strcpy(cwd, cwd_str.c_str());

    char* path = strcat(cwd, "/DROP_DATABASE.py");
    char python[8] { "python " };
    char* command = strcat(python, path);
    std::system(command);

    std::system("pip uninstall -r ./requirements.txt -y");

    delete [] cwd;
    delete [] path;
    return 0;
}