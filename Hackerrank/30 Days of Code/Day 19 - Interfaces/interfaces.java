class Calculator implements AdvancedArithmetic {
    public int divisorSum(int n) {
        int i;
        int[] arr = new int[n];
        for (i = 1; i <= n; i++) {
            if (n % i == 0) {
                arr[i - 1] = i;
            } else {
                arr[i - 1] = 0;
            }
        }
        int sum = 0;
        for (i = 0; i < n; i++) {
            sum += arr[i];
        }
        return sum;
    }
}
