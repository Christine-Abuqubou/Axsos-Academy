public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app.
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly.";
        String readyMessage = ", your order is ready!";
        String displayTotalMessage = "Your total is $";

        
        double mochaPrice = 3.5;
        double dripCoffeePrice = 2.0;
        double lattePrice = 4.5;
        double cappuccinoPrice = 5.0;

        
        String customer1 = "Shatha";
        String customer2 = "Ahmad";
        String customer3 = "Sali";
        String customer4 = "Adam";

        
        boolean isReadyOrder1 = false;  
        boolean isReadyOrder2 = true;   
        boolean isReadyOrder3 = false;  
        boolean isReadyOrder4 = true;   

        

        
        System.out.println(generalGreeting + customer1); 
        

        
        System.out.println(generalGreeting + customer3);
        if (isReadyOrder3) {
            System.out.println(customer3 + readyMessage);
        } else {
            System.out.println(customer3 + pendingMessage);
        }

        
        System.out.println("\n" + generalGreeting + customer2);
        if (isReadyOrder2) {
            System.out.println(customer2 + readyMessage);
            System.out.println(displayTotalMessage + cappuccinoPrice);
        } else {
            System.out.println(customer2 + pendingMessage);
        }

        
        double saliTotal = lattePrice * 2;
        System.out.println("\n" + customer3 + ", " + displayTotalMessage + saliTotal);
        if (isReadyOrder3) {
            System.out.println(customer3 + readyMessage);
        } else {
            System.out.println(customer3 + pendingMessage);
        }

        
        
    }
}
