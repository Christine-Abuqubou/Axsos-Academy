public class Phone extends Device {

    
    public void makeCall() {
        if (battery <= 0) {
            System.out.println("Battery dead. Please charge the phone.");
            return;
        }
        battery -= 5;
        if (battery < 0) battery = 0;
        System.out.println("You make a call.");
        displayBattery();
        checkBatteryCritical();
    }

    public void playGame() {
        if (battery < 25) { 
            System.out.println("Battery too low to play a game. Please charge first.");
            displayBattery();
            return;
        }
        battery -= 20;
        if (battery < 0) battery = 0;
        System.out.println("You play a game.");
        displayBattery();
        checkBatteryCritical();
    }

    public void charge() {
        battery += 50;
        if (battery > 100) battery = 100;
        System.out.println("You charge the phone.");
        displayBattery();
    }

    private void checkBatteryCritical() {
        if (battery < 10) {
            System.out.println(" Battery critical! Please charge soon.");
        }
    }
}
