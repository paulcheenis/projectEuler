public class smallestMultiple {
    public int findNumber(int highestMultiple) {
        int datNumber = 1;
        int finNumber = 0;
        int multiple = 1;

        while (multiple <= highestMultiple) {
            if (datNumber % multiple == 0) {
                multiple++;
            } else {
                multiple = 1;
                datNumber++;
            }
        }
        return datNumber;

    }
    
        
    public static void main(String[] args) {
        smallestMultiple newObj = new smallestMultiple();
        int foundNum = newObj.findNumber(10);
        System.out.println(foundNum); // expect 2520
        foundNum = newObj.findNumber(20);
        System.out.println(foundNum);
    }

}