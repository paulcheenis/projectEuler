import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class totalNameScore { // parent class for inheritance
    static int calcTotal(ArrayList<String> nameArray) { // static method, no need for class instance
        int total = 0;
        for (int i = 0; i < nameArray.size(); i++) { // for every name in the ArrayList
            int multiplier = i; // to be used to multiply the name score
            // i.e. the 938th name is multiplied by the score and 938
            String name = nameArray.get(i);
            int namescore = 0;
            System.out.println(name);

            for (int j = 0; j < name.length(); j++) { // for each letter in the name
                char letter = name.charAt(j);
                System.out.println(letter);
                switch (letter) {
                    case 'A':
                        namescore += 1;
                        break;
                    case 'B':
                        namescore += 2;
                        break;
                    case 'C':
                        namescore += 3;
                        break;
                    case 'D':
                        namescore += 4;
                        break;
                    case 'E':
                        namescore += 5;
                        break;
                    case 'F':
                        namescore += 6;
                        break;
                    case 'G':
                        namescore += 7;
                        break;
                    case 'H':
                        namescore += 8;
                        break;
                    case 'I':
                        namescore += 9;
                        break;
                    case 'J':
                        namescore += 10;
                        break;
                    case 'K':
                        namescore += 11;
                        break;
                    case 'L':
                        namescore += 12;
                        break;
                    case 'M':
                        namescore += 13;
                        break;
                    case 'N':
                        namescore += 14;
                        break;
                    case 'O':
                        namescore += 15;
                        break;
                    case 'P':
                        namescore += 16;
                        break;
                    case 'Q':
                        namescore += 17;
                        break;
                    case 'R':
                        namescore += 18;
                        break;
                    case 'S':
                        namescore += 19;
                        break;
                    case 'T':
                        namescore += 20;
                        break;
                    case 'U':
                        namescore += 21;
                        break;
                    case 'V':
                        namescore += 22;
                        break;
                    case 'W':
                        namescore += 23;
                        break;
                    case 'X':
                        namescore += 24;
                        break;
                    case 'Y':
                        namescore += 25;
                        break;
                    case 'Z':
                        namescore += 26;
                        break;  
                }
            }
            total += multiplier * namescore;
        }
        return total;
    }
}

public class namesScores extends totalNameScore { // main class inherits the parent class 
    // only one public class is allowed in one .java file, and must have same name as file
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
            //System.out.println(nameArray);
            //System.out.println(calcTotal(nameArray));
            myReader.close();


        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }


    }
}