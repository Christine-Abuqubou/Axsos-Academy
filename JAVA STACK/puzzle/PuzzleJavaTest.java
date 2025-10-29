import java.util.ArrayList;

public class PuzzleJavaTest {
    public static void main(String[] args) {
        PuzzleJava generator = new PuzzleJava();

        System.out.println(" Ten Rolls:");
        System.out.println(generator.getTenRolls());

        
        System.out.println("\n Random Letter:");
        System.out.println(generator.getRandomLetter());

        System.out.println("\n Generated Password:");
        System.out.println(generator.generatePassword());

        System.out.println("\n Password Set of 5:");
        System.out.println(generator.getNewPasswordSet(5));

        System.out.println("\n Shuffle Array:");
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            numbers.add(i);
        }
        System.out.println("Before shuffle: " + numbers);
        System.out.println("After shuffle:  " + generator.shuffleArray(numbers));
    }
}
