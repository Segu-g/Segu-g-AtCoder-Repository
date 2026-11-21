#include <iostream>
#include <set>
#include <vector>

int main() {
    int64_t n, l, r;
    std::vector<int64_t> a_arr;

    std::cin >> n >> l >> r;
    for (int i=0; i<n; i++) {
        int64_t a;
        std::cin >> a;
        a_arr.push_back(a);
    }

    std::vector<int64_t> cumsum_arr;
    cumsum_arr.push_back(0);
    for (auto&& a: a_arr) {
        cumsum_arr.push_back(cumsum_arr[cumsum_arr.size() - 1] + a);
    }

    std::vector<int64_t> arr;
    for (int i=0; i<n; i++) {
        cumsum_set.
    }


     
}