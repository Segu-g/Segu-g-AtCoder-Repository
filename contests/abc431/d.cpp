
#include <iostream>
#include <iomanip>
#include <cstdint>
#include <vector>
#include <utility>
#include <algorithm>
#include <numeric>


int main() {
    int n;
    std::cin >> n;

    std::vector<int> w_arr = std::vector<int>(n);
    std::vector<int> h_arr = std::vector<int>(n);
    std::vector<int> b_arr = std::vector<int>(n);

    for (int i=0; i<n; i++) {
        std::cin >> w_arr[i] >> h_arr[i] >> b_arr[i];
    }
    
    int w_sum = std::reduce(w_arr.cbegin(), w_arr.cend());

    std::vector<int64_t> weight_dp = std::vector<int64_t>(w_sum * 2 + 1);
    std::vector<int64_t> next_weight_dp = std::vector<int64_t>(w_sum * 2 + 1);
    for (int i=0; i<2*w_sum+1; i++) {
        weight_dp[i] = INT64_MIN;
    }
    weight_dp[w_sum] = 0;
    
    for (int p=0; p<n; p++) {
        int w = w_arr[p];
        int h = h_arr[p];
        int b = b_arr[p];
        for (int i=0; i< 2*w_sum + 1; i++) {
            next_weight_dp[i] = weight_dp[i];
            if (0 <= i - w) {
                next_weight_dp[i] = std::max(weight_dp[i - w] + b, next_weight_dp[i]);
            } 
            if (i + w < 2 * w_sum + 1) {
                next_weight_dp[i] = std::max(next_weight_dp[i], weight_dp[i + w] + h);
            }
        }
        std::swap(weight_dp, next_weight_dp);
        // for (auto element: weight_dp) {
        //     std::cout << std::setw(3) << std::max<int64_t>(0, element) << " ";
        // }
        // std::cout << std::endl;
    }
    
    std::cout << std::max_element(weight_dp.cbegin() + w_sum, weight_dp.cend())[0];
}