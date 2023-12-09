#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
  std::string input = "./input.txt";

  if (argc > 1) {
    input = argv[1];
  }

  std::fstream file(input);
  std::string line;

  int score_a = 0;
  int score_b = 0;

  // ...
  while (std::getline(file, line)) {
    char a = line[0] - 'A';
    char b = line[2] - 'X';

    score_a += b + 1;               // shape
    score_a += (b + 4 - a) % 3 * 3; // result

    score_b += (b + 2 + a) % 3 + 1; // shape
    score_b += b * 3;               // result
  }

  std::cout << "A: " << score_a << std::endl;
  std::cout << "B: " << score_b << std::endl;

  return 0;
}
