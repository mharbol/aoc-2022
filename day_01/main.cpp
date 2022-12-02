#include<iostream>
#include<fstream>
#include<string>

unsigned long get_max_from_input();

int main(int argc, char const *argv[])
{
    std::cout << "The max is: " << get_max_from_input() << std::endl;

    return 0;    
}

unsigned long get_max_from_input()
{
   std::ifstream file;
   
   unsigned long current_max = 0;

    file.open("day_01_input.txt");

    if (file.is_open())
    {
        std::string read_line;

        // the current sum for the given chunk of calories
        unsigned long accumulator = 0;

        // reading std::getline() gives me an unformatted string input
        while (std::getline(file, read_line))
        {
            // reset accumulator and compare to max for ended chunk of bar calories
            if (read_line.empty())
            {
                // std::cout << accumulator << std::endl;
                if (accumulator > current_max) current_max = accumulator;
                accumulator = 0;
            }
            else
            {
                accumulator += std::stoul(read_line);
            }
        }
    } 
    file.close();

    return current_max;
}