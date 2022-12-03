#include<iostream>
#include<string>
#include<unordered_map>
#include<fstream>

// probably will start doing my declares and includes in a header file soon
// also playing with the "uintXX_t" style for unsighed longs/ints since I see that a lot
uint32_t winning_move(uint32_t);
uint32_t losing_move(uint32_t);
uint32_t elf_rps_orig(uint32_t, uint32_t);
uint32_t elf_rps_next(uint32_t, uint32_t);
uint32_t elf_rps_orig_str(std::string);
uint32_t elf_rps_next_str(std::string);

const uint32_t ROCK = 1;
const uint32_t PAPER = 2;
const uint32_t SCISSORS = 3;

const uint32_t LOSS = 0;
const uint32_t DRAW = 3;
const uint32_t WIN = 6;

int main(int argc, char const *argv[])
{

    uint32_t accumulator_orig = 0;
    uint32_t accumulator_next = 0;

    // going to have to make a file reader utility, not doing this each time
    std::ifstream file;
    file.open("day_02_input.txt");

    if (file.is_open())
    {
        std::string line;

        while (std::getline(file, line))
        {
            // loop through each and update accumulators
            accumulator_orig += elf_rps_orig_str(line);
            accumulator_next += elf_rps_next_str(line);
        }
    }
    file.close();

    std::cout << "Result Part 1: " << accumulator_orig << std::endl;
    std::cout << "Result Part 2: " << accumulator_next << std::endl;
}

// there are better ways to do this, but I want to get good
// at maps early before I need them
std::unordered_map<char, uint32_t> LETTER_TO_MOVE = 
    {
        {'A', ROCK},
        {'B', PAPER},
        {'C', SCISSORS},
        {'X', ROCK},
        {'Y', PAPER},
        {'Z', SCISSORS},
    };

std::unordered_map<char, uint32_t> LETTER_TO_OUTCOME = 
    {
        {'A', ROCK},
        {'B', PAPER},
        {'C', SCISSORS},
        {'X', LOSS},
        {'Y', DRAW},
        {'Z', WIN},
    };

// used to show winning and losing moves based on the cyclical nature of the
// rock paper scissors game. The one to the right is the winning move and the
// one to the left is the losing move
const uint32_t MOVE_CIRCLE[] = {ROCK, PAPER, SCISSORS};

// returns winning move value
 uint32_t winning_move(uint32_t against)
 {
    // since the moves are already their index + 1, the value (against) is the one to the right
    return MOVE_CIRCLE[against % 3];
 }

// returns losing move value
uint32_t losing_move(uint32_t against)
{
    // similar to win it will be (against - 2) for the losing. Mod 3 that is just +1
    return MOVE_CIRCLE[(against + 1) % 3];
}

// assuming we are the player on the right, returns the score based on the rules
 uint32_t elf_rps_orig(uint32_t left_move, uint32_t right_move)
 {
    // DRAW case
    if (left_move == right_move) return right_move + DRAW;

    // WIN case
    if (right_move == winning_move(left_move)) return right_move + WIN;

    // LOSS case
    return right_move; // + LOSS (if it feels lonely otherwise)
 }

 // returns the outcome based on the part 2 rules of the game
 uint32_t elf_rps_next(uint32_t opponent_move, uint32_t expected_outcome)
 {
    // DRAW case
    if (expected_outcome == DRAW) return opponent_move + DRAW;

    // WIN case
    if (expected_outcome == WIN) return winning_move(opponent_move) + WIN; // this shortcuts to my move and the WIN const

    // LOSS case
    return losing_move(opponent_move); // + LOSS (if you like)
 }

 // returns the elf rock paper scissors according to the original strategy
 uint32_t elf_rps_orig_str(std::string str)
 {
    // use the map to get the correct value and put into elf_rps_orig()
    return elf_rps_orig(LETTER_TO_MOVE[str[0]], LETTER_TO_MOVE[str[2]]);
 }

 // returns the elf rock paper scissors according to the new strategy
 uint32_t elf_rps_next_str(std::string str)
 {
    // use the map to get the correct value and put into elf_rps_next()
    return elf_rps_next(LETTER_TO_OUTCOME[str[0]], LETTER_TO_OUTCOME[str[2]]);
 }