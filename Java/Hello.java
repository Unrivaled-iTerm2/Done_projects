package Java;

import java.io.*;
public class Hello {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.valueOf(br.readLine());
        int i = 0;
        while(i < x) {
            System.out.println("Hello, world!");
            i++;
        }
    }
}
