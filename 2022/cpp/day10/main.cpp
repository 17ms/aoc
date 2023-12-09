#include <array>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

void tick(int &cycle, int &v, int &reg, int &sum,
          std::array<std::array<char, 40>, 6> &output) {
  reg += v;
  v = 0;

  int write_pos = cycle - 1;

  if (abs((reg - (write_pos % 40))) <= 1) {
    output[write_pos / 40][write_pos % 40] = '#';
  } else {
    output[write_pos / 40][write_pos % 40] = '.';
  }

  if (cycle % 40 == 20) {
    sum += cycle * reg;
  }

  cycle++;
}

int main(int argc, char *argv[]) {
  std::string input = "./input.txt";

  if (argc > 1) {
    input = argv[1];
  }

  std::fstream file(input);
  std::string line;

  int cycle = 1, x = 1, v = 0, sum = 0;
  std::array<std::array<char, 40>, 6> output;

  while (std::getline(file, line)) {
    std::string cmd = line.substr(0, 4);

    if (cmd == "noop") {
      tick(cycle, v, x, sum, output);
    } else {
      tick(cycle, v, x, sum, output);
      tick(cycle, v, x, sum, output);

      v = std::stoi(line.substr(5, 3));
    }
  }

  std::cout << "A: " << sum << std::endl;
  std::cout << "B:" << std::endl;

  for (size_t i = 0; i < output.size(); ++i) {
    for (size_t j = 0; j < output[i].size(); ++j) {
      std::cout << output[i][j];
    }

    std::cout << std::endl;
  }

  return 0;
}
