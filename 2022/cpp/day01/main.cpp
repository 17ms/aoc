#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

int main(int argc, char *argv[]) {
  std::string input = "./input.txt";

  if (argc > 1) {
    input = argv[1];
  }

  std::fstream file(input);
  std::string line;

  std::vector<int> max;
  int total = 0;

  while (std::getline(file, line)) {
    if (line.size() == 0) {
      max.push_back(total);
      total = 0;

      continue;
    }

    total += std::stoi(line);
  }

  std::nth_element(max.begin(), max.begin() + 3, max.end(),
                   std::greater<int>());
  int sum = max[0] + max[1] + max[2];

  std::cout << "A: " << max[0] << std::endl;
  std::cout << "B: " << sum << std::endl;

  return 0;
}
