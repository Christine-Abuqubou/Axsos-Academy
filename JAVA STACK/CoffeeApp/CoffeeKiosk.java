import java.util.ArrayList;

public class CoffeeKiosk {
    private ArrayList<Item> menu;
    private ArrayList<Order> orders;

    public CoffeeKiosk() {
        this.menu = new ArrayList<Item>();
        this.orders = new ArrayList<Order>();
    }

    public void addMenuItem(String name, double price) {
        Item newItem = new Item(name, price);
        newItem.setIndex(menu.size());
        menu.add(newItem);
    }

    public void displayMenu() {
        for (Item item : menu) {
            System.out.println(item);
        }
    }

    public void newOrder() {
        if (System.console() == null) {
            System.err.println("  System.console() is null. Please run this in a real terminal, not in your IDE.");
            return;
        }

        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();

        Order order = new Order(name);

        displayMenu();

        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();

        while (!itemNumber.equals("q")) {
            try {
                int index = Integer.parseInt(itemNumber);
                if (index >= 0 && index < menu.size()) {
                    Item orderedItem = menu.get(index);
                    order.addItem(orderedItem);
                    System.out.println(orderedItem.getName() + " added to order.");
                } else {
                    System.out.println("Invalid item number. Try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number or 'q' to quit.");
            }

            System.out.println("Enter another item index or q to quit:");
            itemNumber = System.console().readLine();
        }

        System.out.println("Order complete!");
        order.display();
        orders.add(order);
    }

    // Ninja Bonus
    public void addMenuItemByInput() {
        if (System.console() == null) {
            System.err.println("  System.console() is null. Please run this in a real terminal, not in your IDE.");
            return;
        }

        System.out.println("Enter new menu item name:");
        String name = System.console().readLine();

        System.out.println("Enter price for " + name + ":");
        String priceInput = System.console().readLine();

        try {
            double price = Double.parseDouble(priceInput);
            addMenuItem(name, price);
            System.out.println("Item added successfully!");
        } catch (NumberFormatException e) {
            System.out.println("Invalid price input. Please try again.");
        }
    }
}
