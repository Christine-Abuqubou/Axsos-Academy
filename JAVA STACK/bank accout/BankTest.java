public class BankTest {
    public static void main(String[] args){
        // Create 3 bank accounts
        BankAccount acount1 = new BankAccount();
        BankAccount acount2 = new BankAccount();
        BankAccount acount3 = new BankAccount();

        // Deposit Test
        acount1.deposit(13.2);
        acount1.display();
        // - each deposit should increase the amount of totalMoney

        // Withdrawal Test
        // - withdraw some money from each bank account's checking or savings account and display the remaining balance
        // - each withdrawal should decrease the amount of totalMoney

        // Static Test (print the number of bank accounts and the totalMoney)

    }
}