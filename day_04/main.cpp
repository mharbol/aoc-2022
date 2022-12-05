#include<iostream>
#include<fstream>
#include<string>

// Not doing header just for a few declarations. Here we go
int* listify(std::string line);
uint32_t envelop(int l0, int r0, int l1, int r1);
uint32_t overlap(int l0, int r0, int l1, int r1);

int main(int argc, char const *argv[])
{
    // Also, I know this was the last time I said I'd do this but...
    // we'll address that all later
    std::ifstream file;
    file.open("day_04_input.txt");

    if (file.is_open())
    {
        std::string line;

        while (std::getline(file, line))
        {
            // do things

        }
    }
    file.close();
}

// Turns the stylized string into an array that holds the 4 values in question
int* listify(std::string line)
{
    // this is going to be really rough...
}