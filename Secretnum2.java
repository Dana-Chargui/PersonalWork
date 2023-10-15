import javax.swing.JOptionPane;
import java.util.Random;


public class Secretnum2 {
    public static void main(String[] args) {
        
        Random random = new Random();
        int secret = random.nextInt(9)+1;
        int tries = 3;
        for (int i=0;i<tries;i++){
            int guess = Integer.parseInt(JOptionPane.showInputDialog("Enter a number between 1-10"));
            if(guess==secret){
                JOptionPane.showInternalMessageDialog(null,"You win! the correct guess was "+secret);
                break;
            } else {
                JOptionPane.showInternalMessageDialog(null,"Try again!");
                String response = JOptionPane.showInputDialog("Press q or Q to exit out of the game");
                if(response.equals("q") || response.equals("Q")){
                    System.out.println("You exit out of the game");
                    break;
                } else {
                    System.out.println("You are still in the game");
                    
                }
            }
        }
        
    }
}
