import java.util.Scanner;

public class GCD {
    static Scanner input = new Scanner(System.in);
    
    public static void main(String [] args){
        gcd();
    }
    
           public static void gcd(){
        System.out.println("Enter two numbers to find their greatest common denominator");
        
        //  The gcd will hold the greatest common deniminator of both numbers and is initially set to 1
        int gcd = 1;
        
        System.out.println("Enter the first number");
        //  The num1 variable holds the first number supplied by the user.
        int num1 = input.nextInt();
        
        System.out.println("Enter the first number");
        //  The num2 variable holds the second number supplied by the user.
        int num2 = input.nextInt();
        
        //  The for loop is executed until i is less that both num1 and num2, which ensures that all the numbers between 1 and
        //  the smallest of the two numbers are iterated to find the GCD.
        for(int i = 1; i <= num1 && i <= num2; i++){
            
            //  Checks if i is a factor of both numbers entered by the user
            if(num1 % i == 0 && num2 % i == 0){
                gcd = i;
            }
        }
        
        System.out.println("The greatest common denominator of " + num1 + " and " + num2 + " is " + gcd);
    }
}  
