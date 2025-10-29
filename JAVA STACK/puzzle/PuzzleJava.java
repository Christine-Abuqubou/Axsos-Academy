import java.util.ArrayList;
import java.util.Random;

public class PuzzleJava {

    public ArrayList<Integer> getTenRolls() {
        Random randMachine = new Random();
        ArrayList<Integer> rolls = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            int randomNum = randMachine.nextInt(20) + 1; 
            rolls.add(randomNum);
        }
        return rolls;
    }

    public char getRandomLetter() {
        Random randMachine = new Random();
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        int randomIndex = randMachine.nextInt(26);
        return alphabet[randomIndex];
    }

    public String generatePassword() {
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < 8; i++) {
            password.append(getRandomLetter());
        }
        return password.toString();
    }

    public ArrayList<String> getNewPasswordSet(int length) {
        ArrayList<String> passwordSet = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            passwordSet.add(generatePassword());
        }
        return passwordSet;
    }

    public ArrayList<Integer> shuffleArray(ArrayList<Integer> array) {
        Random randMachine = new Random();
        for (int i = 0; i < array.size(); i++) {
            int randomIndex = randMachine.nextInt(array.size());
            int temp = array.get(i);
            array.set(i, array.get(randomIndex));
            array.set(randomIndex, temp);
        }
        return array;
    }
}
