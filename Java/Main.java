package Java;

import java.io.*;
import java.util.Random;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("I'll choose a number. From 1 to 30.");
        System.out.println("Now you need to guess the number what I chose.");
        System.out.println("Ready?");
        System.out.println("Start!");
        Random random = new Random();
        int guessed_number;
        int chosen_number = random.nextInt(30) + 1;
        while(true) {
            try {
                guessed_number = Integer.valueOf(br.readLine());
                if (guessed_number < chosen_number) {
                    System.out.println("It's small. Make it bigger and try again.");
                }
                else if (guessed_number > chosen_number) {
                    System.out.println("It's big. Make it smaller and try again.");
                }
                else if (guessed_number == chosen_number) {
                    System.out.println("Yes! You got it! You guessed it right!");
                    System.out.println("-GAME END-");
                    break;
                }
            }
            catch(Exception e) {
                System.out.println("Invalid input.");
            }
            
        }
    }
}