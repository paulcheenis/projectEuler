public class sumSquareDiff {
    public double sumOfSquares(int max) {
        double total = 0;
        for (int i = 1; i <= max; i++) {
            double square = i*i;
            total = total + square;
        }
        return(total);
    }
    
    public double squareOfSum(int max) {
        double total = 0;
        double total_sq = 0;
        for (int j = 1; j <= max; j++) {
            total = total + j;
        }
        total_sq = total * total;
        return(total_sq);
    }

    public static void main(String[] args) {
        sumSquareDiff mathObj = new sumSquareDiff();
        double sum1 = mathObj.sumOfSquares(100);
        double sum2 = mathObj.squareOfSum(100);
        double diff = sum2 - sum1;
        System.out.println(diff);
    }
}