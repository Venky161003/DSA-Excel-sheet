class Solution {
  public:
    int findPosition(int N) {
        int count = 0
        int position = 0
        while (N > 0) {
            if (N & 1) {
                count++
                if (count > 1) return -1
            }
            N >>= 1
            position++
        }
        return (count == 1) ? position : -1
    }
};
