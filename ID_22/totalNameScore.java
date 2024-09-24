import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class totalNameScore {
    public int total(arrayList<String>) {
        for (int i = 0; i <= arrayList.size(); i++) {
            for
        }
    }
}


public class namesScores {
    public static void main(String[] args) {
        try {
            File myObj = new File("namesscores.txt");
            Scanner myReader = new Scanner(myObj);
            ArrayList<String> nameArray = new ArrayList<String>();
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                nameArray.add(data);
                //System.out.println(data);
            }
            System.out.println(nameArray);
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }
}