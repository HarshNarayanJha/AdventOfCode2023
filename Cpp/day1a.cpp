#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>

std::string digits = "1234567890";

int main()
{
    std::vector<std::string> lines;
    std::vector<int> numbers;

    std::string line;

    std::ifstream InputRead;

    InputRead.open("../input1.txt");

    while (std::getline(InputRead, line)) {
        lines.push_back(line);
    }

    InputRead.close();

    for (int i = 0; i < lines.size(); ++i)
    {
        char first = 'x';
        char last = 'x';
        std::string line = lines[i];
        std::string thenumbers;
        // std::cout << lines[i] << std::endl;
        for (int j = 0; j < lines[i].size(); ++j)
        {
            char c = line[j];
            if (isdigit(c) && first == 'x') {
                first = c;
            } else if (isdigit(c)) {
                last = c;
            }
        }

        if (last == 'x') last = first;

        thenumbers.push_back(first);
        thenumbers.push_back(last);

        // std::cout << first << last << std::endl;
        // std::cout << thenumbers << std::endl;

        numbers.push_back(std::stoi(thenumbers));
    }

    int32_t sum = std::accumulate(numbers.begin(), numbers.end(), 0);

    std::cout << "Solution: " << sum << std::endl;

    return 0;
}