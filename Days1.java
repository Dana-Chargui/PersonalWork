package java.util;
import java.util.Scanner;

class Days {
    public static void main(String[] args){
        java.util.Scanner enter = new java.util.Scanner(System.in);
        System.out.println("Enter the year month and day ");
        int year = enter.nextInt();
        int month = enter.nextInt();
        int day = enter.nextInt();
        int nbd=0;
        switch (month){
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                System.out.println( month + " month has 31 days");
                nbd=31;
                break;
            case 4: case 6: case 9: case 11:
                System.out.println( month + " month has 30 days");
                nbd=30;
                break;
            case 2:
                if ((year%4==0) && ((year%100!=0 || year%400==0))){
                    System.out.println("Leap year! Febuary has 29 days");
                    nbd=29;
                } else {
                    System.out.println(month + " month has 28 days");
                    nbd=28;
                }
                break;
            default:
                System.out.println("Invalid month");
                break;
            }
        System.out.println(day + "/" + month + "/" + year);
    }
}
