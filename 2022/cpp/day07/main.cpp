#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

void add_sums(std::vector<std::string> path,
              std::unordered_map<std::string, int> &dirs, int size) {
  while (!path.empty()) {
    std::string path_str =
        std::accumulate(path.cbegin(), path.cend(), std::string(""));

    if (auto it = dirs.find(path_str); it != dirs.end()) {
      dirs[path_str] += size;
    } else {
      dirs.insert(std::make_pair(path_str, size));
    }

    path.pop_back();
  }
}

int main(int argc, char *argv[]) {
  std::string input = "./input.txt";

  if (argc > 1) {
    input = argv[1];
  }

  std::fstream file(input);
  std::string line;

  std::vector<std::string> path;
  std::unordered_map<std::string, int> dirs;

  while (std::getline(file, line)) {
    if (line[0] != '$' && line[0] != 'd') {
      int end = line.find(' ');
      int size = std::stoi(line.substr(0, end));

      add_sums(path, dirs, size);
    } else if (line.substr(0, 4) == "$ cd") {
      std::string new_dir = line.substr(5, 10);

      if (new_dir == "..") {
        path.pop_back();
        continue;
      }

      path.push_back(new_dir + "/");
    }
  }

  int total = 0;
  int req = 30000000 - (70000000 - dirs["//"]);
  std::vector<int> sizes;

  for (auto p : dirs) {
    sizes.push_back(p.second);

    if (p.second <= 100000) {
      total += p.second;
    }
  }

  std::sort(sizes.begin(), sizes.end());
  auto it = std::find_if(sizes.cbegin(), sizes.cend(),
                         [req](int x) { return x > req; });

  std::cout << "A: " << total << std::endl;
  std::cout << "B: " << it[0] << std::endl;
}
