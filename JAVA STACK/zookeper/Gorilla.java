public class Gorilla extends Mammal {

    public Gorilla() {
        super(100);
    }

    public void throwSomething() {
        setEnergy(getEnergy() - 5);
        System.out.println("The gorilla has thrown something! (-5 energy)");
    }

    public void eatBananas() {
        setEnergy(getEnergy() + 10);
        System.out.println("The gorilla is happy after eating bananas! (+10 energy)");
    }

    public void climb() {
        setEnergy(getEnergy() - 10);
        System.out.println("The gorilla has climbed a tree! (-10 energy)");
    }
}
