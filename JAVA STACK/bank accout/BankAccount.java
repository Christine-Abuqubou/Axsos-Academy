public class BankAccount {
    // MEMBER VARIABLES
    private double checkingBalance;
    private double savingsBalance;
    private double amount;

    private static int accounts;
    private static double totalMoney; // refers to the sum of all bank account checking and savings balances

    // CONSTRUCTOR
    // Be sure to increment the number of accounts
    public BankAccount(){
        this.checkingBalance = checkingBalance;
        this.savingsBalance = savingsBalance;
        this.amount = amount;
        accounts ++;
        totalMoney ++;
    }

    // GETTERS
    // for checking, savings, accounts, and totalMoney
    public double getCheckingBalance(){
        return checkingBalance;
    }

    public double getSavigs(){
        return savingsBalance;
    }

    public static int getAccounts(){
        return accounts;
    }

    public static double getTotal(){
        return totalMoney;
    }


    

    // METHODS
    // deposit
    // - users should be able to deposit money into their checking or savings account
    public void deposit(double amount){
        checkingBalance += amount;
    

        savingsBalance += amount;
    }
    // withdraw 
    // - users should be able to withdraw money from their checking or savings account
    // - do not allow them to withdraw money if there are insufficient funds
    // - all deposits and withdrawals should affect totalMoney
    public void withdraw(double amount){
        if(checkingBalance >= amount){
            checkingBalance -= amount;
        }else{
            System.out.println("insufficiant funds");
        }
        if(savingsBalance >= amount){
            savingsBalance -= amount;
        }else{
            System.out.println("insufficiant funds");
        }
    }
    // getBalance
    // - display total balance for checking and savings of a particular bank account

    public void display(){
        System.out.println("checking balance " + checkingBalance);
        System.out.println("saving balance " + savingsBalance);
        System.out.println("total money " + totalMoney);
    }
}