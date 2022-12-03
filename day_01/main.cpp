#include<iostream>
#include<fstream>
#include<string>
#include<vector>

unsigned long get_max_from_input();
std::vector<unsigned long> get_all_sums_from_input();

int main(int argc, char const *argv[])
{
    std::cout << "The max is: " << get_max_from_input() << std::endl;
    
    // trying my hand at sorting
    std::vector<unsigned long> all_sums = get_all_sums_from_input();
    std::sort(all_sums.begin(), all_sums.end());

    // using the end pointer to sum up the last 3 in the vector
    auto index = all_sums.end();
    --index; // the last value is a null terminator dec before looping
    unsigned long acc = 0;

    for (int x = 0 ; x < 3 ; x++)
    {
        acc += *index;
        --index;
    }

    std::cout << "The sum of the top 3 is: " << acc << std::endl;
    
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

// same function with a twist for part 2
std::vector<unsigned long> get_all_sums_from_input()
{
   std::ifstream file;

   std::vector<unsigned long> all_sums;

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
                // addition for part 2. Push the accumulator value to a vector
                all_sums.push_back(accumulator);
                accumulator = 0;
            }
            else
            {
                accumulator += std::stoul(read_line);
            }
        }
    } 
    file.close();

    return all_sums;
}