
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>

#include "day_03.hpp"

int main(int argc, char const *argv[])
{
    // I swear, this is the last time I am parsing a file like this
    std::ifstream file;
    file.open("day_03_input.txt");

    uint32_t part_1_loop = 0;
    uint32_t part_1_set = 0;
    uint32_t part_2_loop = 0;
    std::string strings[3];
    int count = 0;

    if (file.is_open())
    {
        std::string line;

        while (std::getline(file, line))
        {
            // do things
            part_1_loop += priority(rucksack_inventory_nested_loop(line));
            part_1_set += priority(rucksack_inventory_hashset(line));

            // collect strings for checking badges
            strings[count % 3] = line;
            count++;
            if (count % 3 == 0)
            {
                part_2_loop += priority(badge_group_loop(strings[0], strings[1], strings[2]));
            }
        }
    }
    file.close();

    std::cout << "Ruck inventory with loops: " << part_1_loop << std::endl;
    std::cout << "Ruck inventory with set:   " << part_1_set << std::endl;
    std::cout << "Badge number with loops:   " << part_2_loop << std::endl;

    
    return 0;
}

// Priority of the letter using the ASCII values
uint32_t priority(char character)
{
    if ('A' <= character && character <= 'Z')
        return (uint32_t) (character - 'A' + 27);
    
    return (uint32_t) (character - 'a' + 1);
}

// -------------- Part 1 --------------

// For part 1: the left/right inventory using nested loops (gross)
// returns the common char between the right and left hand sides
char rucksack_inventory_nested_loop(std::string inventory)
{
    int halfway = inventory.length() / 2;

    for (int left = 0 ; left < halfway ; left++)
    {
        for (int right = halfway ; right < inventory.length() ; right ++)
        {
            if (inventory[left] == inventory[right])
            {
                return inventory[left];
            }
        }
    }
    // we have bad news if we make it here.
    return '#';
}

// more responsible inventory function
// this won't be super satisfying, I'm a little tired. Going
// to make a set for the left and right and use set_intersection()
// to see what value they have in common

// wanted to do something cool where I inserted until I found the
// duplicate but didn't take into account that either side could
// have multiple letters that were the same on one side and they'd be
// false positives
char rucksack_inventory_hashset(std::string inventory)
{
    std::set<char> left_set, right_set;

    int len = inventory.length();

    // fill either set
    for (int index = 0 ; index < len / 2 ; index++)
    {
        left_set.insert(inventory[index]);
    }
    for (int index = len / 2; index < len ; index++)
    {
        right_set.insert(inventory[index]);
    }

    // this intersects the left and right sets and inserts it into intersection
    std::set<char> intersect;
    std::set_intersection(left_set.begin(), left_set.end(), right_set.begin(),
                          right_set.end(), std::inserter(intersect, intersect.begin()));

    // there SHOULD only be one value in here so return the first one
    return *intersect.begin();
}

// -------------- Part 2 --------------
char badge_group_loop(std::string s1, std::string s2, std::string s3)
{
    // this will be gross but it will work
    // loop over s1 and s2, put their intersections in "first_inter"
    // then loop over first_inter and s3 and return the common char
    std::vector<char> first_inter;

    for (char letter : s1)
    {
        if (s2.find(letter) != std::string::npos) // npos is none found
        {
            first_inter.push_back(letter);
        }
    }

    // second loop
    for (char letter : first_inter)
    {
        if (s3.find(letter) != std::string::npos)
        {
            return letter;
        }
    }
    // we're screwed if we're here
    return '#';
}
