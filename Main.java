import java.util.Random;


public class Main {

    public static void main(String args[]){

        Random rand = new Random();
  
        for (int i=0; i<100; i++) {

            int rand_int = rand.nextInt();

            System.out.println(rand_int);
            
        }

    }

}