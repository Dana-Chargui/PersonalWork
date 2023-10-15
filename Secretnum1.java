import java.util.Random;
import javax.swing.JOptionPane;

public class Secretnum {
    public static void main(String[] args) {
        Random random = new Random();
        int secret = random.nextInt(9)+1;
        
        int guess = Integer.parseInt(JOptionPane.showInputDialog("Enter a number between 1-10"));
        if(guess==secret){
            JOptionPane.showInternalMessageDialog(null,"You win! the correct guess was "+secret);
        } else {
            JOptionPane.showInternalMessageDialog(null,"You lost! the correct guess was "+secret);
        }
    }
}
