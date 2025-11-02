import java.util.ArrayList;

public class Order {
    private String name;
    private ArrayList<Item> items;

    public Order(String name) {
        this.name = name;
        this.items = new ArrayList<Item>();
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public String getName() {
        return name;
    }

    public double getTotal() {
        double total = 0;
        for (Item item : items) {
            total += item.getPrice();
        }
        return total;
    }

    public void display() {
        System.out.println("\nCustomer Name: " + name);
        for (Item item : items) {
            System.out.printf("%s - $%.2f\n", item.getName(), item.getPrice());
        }
        System.out.printf("Total: $%.2f\n", getTotal());
    }
}
