import java.util.ArrayList;

public class CafeUtil {  // ← Class starts here

    // ====== 1. getStreakGoal ======
    public int getStreakGoal() {
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
        }
        return sum;
    }

    // Ninja Bonus: adjustable weeks
    public int getStreakGoal(int numWeeks) {
        int sum = 0;
        for (int i = 1; i <= numWeeks; i++) {
            sum += i;
        }
        return sum;
    }

    // ====== 2. getOrderTotal ======
    public double getOrderTotal(double[] prices) {
        double total = 0;
        for (double price : prices) {
            total += price;
        }
        return total;
    }

    // ====== 3. displayMenu ======
    public void displayMenu(ArrayList<String> menuItems) {
        for (int i = 0; i < menuItems.size(); i++) {
            System.out.println(i + " " + menuItems.get(i));
        }
    }

    public boolean displayMenu(ArrayList<String> menuItems, ArrayList<Double> prices) {
        if (menuItems.size() != prices.size()) {
            System.out.println("Error: Menu and prices size mismatch.");
            return false;
        }
        for (int i = 0; i < menuItems.size(); i++) {
            System.out.printf("%d %s -- $%.2f\n", i, menuItems.get(i), prices.get(i));
        }
        return true;
    }

    // ====== 4. addCustomer ======
    public void addCustomer(ArrayList<String> customers) {
        System.out.println("Enter your name please:");
        String username = System.console().readLine(); // works from terminal
        System.out.println("Hello, " + username + "!");
        System.out.println("There are " + customers.size() + " people in front of you.");
        customers.add(username);
        System.out.println(customers);
    }

    // ====== Bonus: printPriceChart ======
    public void printPriceChart(String product, double price, int maxQuantity) {
        System.out.println(product);
        for (int i = 1; i <= maxQuantity; i++) {
            double total = price * i;
            System.out.printf("%d - $%.2f\n", i, total);
        }
    }

}  // ← Class ends here
