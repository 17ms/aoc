#include <fstream>
#include <iostream>
#include <regex>
#include <stack>

void move_containers(std::vector<std::stack<char>> &stacks_a,
                     std::vector<std::stack<char>> &stacks_b, int n, int a,
                     int b) {
  std::vector<char> tmp;

  for (int i = 0; i < n; ++i) {
    stacks_a[b - 1].push(stacks_a[a - 1].top());
    stacks_a[a - 1].pop();

    tmp.push_back(stacks_b[a - 1].top());
    stacks_b[a - 1].pop();
  }

  for (auto i = tmp.rbegin(); i != tmp.rend(); ++i) {
    stacks_b[b - 1].push(*i);
  }
}

std::vector<std::stack<char>>
reverse_stacks(std::vector<std::stack<char>> stacks) {
  std::stack<char> tmp;
  char c;

  for (size_t i = 0; i < stacks.size(); ++i) {
    while (!stacks[i].empty()) {
      c = stacks[i].top();
      stacks[i].pop();
      tmp.push(c);
    }

    stacks[i] = tmp;
    tmp = std::stack<char>();
  }

  return stacks;
}

int main(int argc, char *argv[]) {
  std::string input = "./input.txt";

  if (argc > 1) {
    input = argv[1];
  }

  std::fstream file(input);
  std::string line;

  bool is_stack = true;
  std::regex cmd("move (\\d+) from (\\d+) to (\\d+)");
  std::smatch m;

  std::vector<std::stack<char>> stacks_a;
  std::vector<std::stack<char>> stacks_b;

  while (std::getline(file, line)) {
    if (line[1] == '1') {
      stacks_a = reverse_stacks(stacks_a);
      stacks_b = stacks_a;
      is_stack = false;

      std::getline(file, line); // skip the empty line
      continue;
    }

    if (is_stack) {
      for (size_t i = 0; i < line.size(); ++i) {
        if (const char c = line[i]; c == '[') {
          size_t pos = i / 4;

          if (stacks_a.size() <= pos) {
            stacks_a.resize(pos + 1);
          }

          stacks_a[pos].push(line[i + 1]);
        }
      }
    } else {
      std::regex_search(line, m, cmd);

      int n = std::stoi(m[1].str());
      int a = std::stoi(m[2].str());
      int b = std::stoi(m[3].str());

      move_containers(stacks_a, stacks_b, n, a, b);
    }
  }

  std::cout << "A: ";

  for (auto s : stacks_a) {
    std::cout << s.top();
  }

  std::cout << std::endl;

  std::cout << "B: ";

  for (auto s : stacks_b) {
    std::cout << s.top();
  }

  std::cout << std::endl;
}
