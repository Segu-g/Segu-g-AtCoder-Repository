#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

void listup(
    std::vector<int64_t>& current_targets,
    std::vector<std::map<int64_t, std::vector<int64_t>>>& children_dict_arr,
    std::vector<int64_t>& output
) {
    std::sort(current_targets.begin(), current_targets.end());
    for (auto current_target: current_targets) { 
        output.push_back(current_target);
    }

    std::map<int64_t, std::vector<int64_t>> children_dict;
    for (auto current_target: current_targets) {
        for (auto [value, children_list]: children_dict_arr[current_target]) {
            for (auto children: children_list) {
                children_dict[value].push_back(children);
            }
        }
    }

    for (auto [key, value] : children_dict) {
        listup(value, children_dict_arr, output);
    }
    return;
}

int main() {
    int64_t n;
    std::cin >> n;
    std::vector<std::map<int64_t, std::vector<int64_t>>> children_dict_arr(n+1);
    for (int i=0; i<n; i++) {
        int64_t x, y;
        std::cin >> x >> y;
        children_dict_arr[x][y].push_back(i+1);
    }
    std::vector<int64_t> output;
    std::vector<int64_t> initial_targets = {0};
    listup(initial_targets, children_dict_arr, output);

    for (int i=1; i<n; i++) {
        std::cout << output[i] << " ";
    }
    std::cout << output[n] << std::endl;
    return 0;
}