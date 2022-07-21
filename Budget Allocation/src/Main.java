/*
*Import a scanner object to prompt user to input what is required
*Import the arraylist in order to store numerical values entered and obtained from the calculations*/

import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        System.out.println("How much do you want to spend?");/*Prints out the statement in quotes*/
        Scanner scan = new Scanner(System.in);
        double total = scan.nextDouble();
        double sum = 0;/*Initial sum is at 0.0*/
        int i = 0;
        ArrayList<Double> proportion =  new ArrayList<Double>();/*Store our values in the array variable 'proportion'*/
        System.out.println("Enter your proportion of various expenses.");/*Display the statement in quotes*/
        System.out.println("This system stops if cumulative proportion exceeds 100%");/*Display the statement in quotes*/
        do {
            System.out.println("Your proportion of expense "
            + (i + 1) + ":");
            double value = scan.nextDouble();
            proportion.add(value);
            sum += proportion.get(i);
        } while (sum <= 100);
        scan.close();
        if  (sum > 100) {
            double cumulativeSum = 0.0;
            for (int j = 0; j < proportion.size() - 1; j++) {
                cumulativeSum += proportion.get(j);
            }
            proportion.set(proportion.size() - 1,
                    100.0 - cumulativeSum);
        }
        for (double value : proportion) {
            double expense = value * total / 100.0;
            System.out.println("Your final proportion expense "
            + value
            +"% equals $"
            + expense);
        }
    }
}