/**
 * Market Handler
 * Basic text-based simulator of a shopping cart. Program to practice
 * creating basic input/output using Scanner objects.
 * @author Octavian Pullum
 * @version 1.0
 * @since 1.0
 */


import java.util.InputMismatchException;
import java.util.Scanner;

public class Market {

    public static void printMenu() {
        System.out.println("SHOPPING CART MENU");
        System.out.println("1. Add item to the cart");
        System.out.println("2. View items in cart");
        System.out.println("3. Checkout items");
        System.out.println("0. Exit program");
    }

    public static void main(String[] args) {
        Cart shoppingCart = new Cart();             // Shopping cart to store items
        Scanner input = new Scanner(System.in);     // Retrieving user input

        int selection = -1;

        do {
            printMenu();
            System.out.print("\nEnter your selection: ");

            try {
                String line = input.nextLine();
                selection = Integer.parseInt(line);
                if (selection < 0 || selection > 3) {
                    System.out.println("Invalid Selection. Please select a choice from the given options.");
                } else {
                    switch (selection) {
                        case 1:
                            String itemName;
                            double itemPrice;
                            System.out.print("Enter a name for the item: ");
                            itemName = input.nextLine();
                            System.out.print("Enter the item price: ");

                            line = input.nextLine();
                            try {
                                itemPrice = Double.parseDouble(line);
                                shoppingCart.addItem(new Item(itemName, itemPrice));
                            } catch (NumberFormatException err) {
                                System.out.println("Please enter a numerical value for the price");
                                System.out.println("Cancelling item creation...");
                            }

                            break;
                        case 2:
                            Item[] items = shoppingCart.returnCart();
                            if (items.length == 0) {
                                System.out.println("Shopping Cart is Empty!");
                            } else {
                                for (Item item: shoppingCart.returnCart()) {
                                    System.out.println(item);
                                }
                            }
                            break;
                        case 3:
                            System.out.println("CHECKING OUT ITEMS...");
                            double totalPrice = 0;
                            for (Item item : shoppingCart.returnCart()) {
                                System.out.println(item);
                                totalPrice += item.getPrice();
                            }
                            System.out.printf("\n\nFINAL PRICE: %f", totalPrice);
                            shoppingCart = new Cart();

                            break;
                        case 0:
                            System.out.println("STOPPING PROGRAM");
                            break;
                    }
                }
            } catch (NumberFormatException err) {
                System.out.println("Please enter a numerical value between 0 - 3 from the options given.");
            }
        }
        while (selection != 0);
    }
}