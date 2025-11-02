public class Bat extends Mammal {

    public Bat() {
        super(300);
    }

    public void fly() {
        setEnergy(getEnergy() - 50);
        System.out.println("The bat is flying through the night! (-50 energy)");
    }

    public void eatHumans() {
        setEnergy(getEnergy() + 25);
        System.out.println("The bat feasts on a human... (+25 energy)");
    }

    public void attackTown() {
        setEnergy(getEnergy() - 100);
        System.out.println("The bat is attacking a town! (-100 energy)");
    }
}
