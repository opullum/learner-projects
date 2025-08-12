/**
 * Market Handler
 * Basic text-based simulator of a shopping cart. Program to practice
 * creating basic input/output using Scanner objects.
 * @author Octavian Pullum
 * @version 1.0
 * @since 1.0
 */

import java.util.Scanner;

public class Market {

    public static void printMenu() {
        System.out.println("\nSHOPPING CART MENU");
        System.out.println("1. Add item to the cart");
        System.out.println("2. View items in cart");
        System.out.println("3. Checkout items");
        System.out.println("0. Exit program");
    }

    public static void main(String[] args) {
        Cart shoppingCart = new Cart();                             // Shopping cart to store items
        Scanner input = new Scanner(System.in);                     // Retrieving user input

        // Default value of -1 placed here. Will not trigger any options, leading to user input prompt
        int selection = -1;

        do {
            printMenu();
            System.out.print("\nEnter your selection: ");

            try {
                // .nextFoo() will not stop at the ENTER key. Therefore, we convert to relevant data type
                // to clear the scanner
                String line = input.nextLine();
                selection = Integer.parseInt(line);

                // Checking for invalid inputs
                if (selection < 0 || selection > 3) {
                    System.out.println("Invalid Selection. Please select a choice from the given options.\n");
                } else {

                    // INPUT HANDLER (1: Add Item, 2: View Items, 3: Checkout Items, 0: Exit)
                    switch (selection) {
                        case 1:
                            // CASE ONE: CREATING NEW ITEM
                            // Creates a new instance of the Item class to be placed in shoppingCart
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
                            // CASE TWO: LIST SHOPPING CART ITEMS
                            // Displays all Item instances in shoppingCart, which returns an Item[] when
                            // Cart.returnCart() is called
                            Item[] items = shoppingCart.returnCart();
                            if (items.length == 0) {
                                System.out.println("Shopping Cart is Empty!");
                            } else {
                                System.out.println("DISPLAYING SHOPPING CART ITEMS...");
                                for (Item item: shoppingCart.returnCart()) {
                                    System.out.println(item);
                                }
                            }
                            break;
                        case 3:
                            // CASE 3: ITEM CHECKOUT
                            // Displays the total price for all the items. Clears cart afterward.
                            System.out.println("CHECKING OUT ITEMS...");
                            double totalPrice = 0;
                            for (Item item : shoppingCart.returnCart()) {
                                System.out.println(item);
                                totalPrice += item.getPrice();
                            }
                            System.out.printf("\nFINAL PRICE: %f\n", totalPrice);
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