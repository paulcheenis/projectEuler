import java.util.ArrayList;

public class evenFibonacci{

    public int fibonacci(int max) {
        int term1 = 1;
        int term2 = 2;
        int fibsum = term1 + term2;

        ArrayList<Integer> fibSeq = new ArrayList<Integer>(); // Created ArrayList that can be appended
        fibSeq.add(term1); // added term 1 to array
        fibSeq.add(term2); // added term 2 to array
        int total = 0;
        
        while (fibsum < max) {
            fibsum = term1 + term2;
            fibSeq.add(fibsum); // adding term to array
            term1 = term2;
            term2 = fibsum;
        }

        for (int i : fibSeq) {
            if (i % 2 == 0) {
                total = total + i;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        evenFibonacci newObj = new evenFibonacci();
        System.out.println(newObj.fibonacci(4000000));
    }
}