#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

bool is_safe(std::vector<int> numbers) {

  // std::cout << "is_safe: start" << std::endl;
  if (numbers[0] == numbers[1])
    return false;
  bool asc = numbers[0] < numbers[1];
  int i = 0;
  // std::cout << "is_safe: before loop" << std::endl;
  for (int j = 1; j < numbers.size(); j++) {
    i = j - 1;
    // std::cout << "\t" << i << " " << j << std::endl;
    int dist = numbers[i] - numbers[j];
    if (dist == 0)
      return false;
    if ((dist < 0) != asc)
      return false;
    dist = abs(dist);
    if (dist > 3)
      return false;
  }
  return true;
}
template <typename T>
std::ostream &operator<<(std::ostream &out, const std::vector<T> vec) {
  for (T x : vec) {
    std::cout << x << " ";
  }
  // std::cout << std::endl;
  return out;
}

int main(int argc, char **argv) {
  int n1 = 0;
  int total_safe_base = 0;
  int total_safe_subsets = 0;
  std::string line;
  std::ifstream infile("input.txt");
  while (std::getline(infile, line)) {
    std::vector<int> numbers;
    std::istringstream iss(line);
    // line to std::vec<int>
    while (iss >> n1) {
      numbers.push_back(n1);
    }
    bool safety = is_safe(numbers);
    // std::cout << numbers << "\t" << (safety ? "true" : "false") << std::endl;

    if (safety) {
      total_safe_base += 1;
      continue;
    }

    // call is_safe for subsets
    for (int i = 0; i < numbers.size(); i++) {
      std::vector<int> subset;
      for (int j = 0; j < numbers.size(); j++) {
        if (i == j)
          continue;
        subset.push_back(numbers[j]);
      }
      // std::cout << "checking: " << subset;
      if (is_safe(subset)) {
        total_safe_subsets += 1;
        break;
      }
    }
  }
  std::cout << "Total: " << total_safe_base << "+" << total_safe_subsets << "="
            << total_safe_base + total_safe_subsets << std::endl;
}
