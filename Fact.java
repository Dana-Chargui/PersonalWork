import java.util.Scanner;

public class Fact {
    static int Facto(int y) {
        int fact=1;
        for(int i=1;i<=y;i++){
            fact=fact*i;
        }
        return fact;
     }
       
    
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.print("What is the factoriel of : ");
        int x = scan.nextInt();
        int f = Facto(x);
        System.out.println("Factorial of "+x+" is "+f);
    }
}
