import javax.swing.JOptionPane;

public class MyOwn {
    public static void main(String[] args) {        
        //this gives you a pop up to input value into

        String name = JOptionPane.showInputDialog("Enter your name :");
        JOptionPane.showInternalMessageDialog(null,"Hello "+name);
        
        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age :"));
        if (age==1){
        JOptionPane.showInternalMessageDialog(null,"You're "+age+" year old");
        } else {
        JOptionPane.showInternalMessageDialog(null,"You're "+age+" years old");
        }
        
        double height = Double.parseDouble(JOptionPane.showInputDialog("Enter your height :"));
  }
}
