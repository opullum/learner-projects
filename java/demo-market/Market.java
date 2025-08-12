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
        System.out.println("SHOPPING CART MENU");
        System.out.println("1. Add item to the cart");
        System.out.println("2. View items in cart");
        System.out.println("3. Checkout items");
        System.out.println("0. Exit program");
    }

    public static void main(String[] args) {
        Cart shoppingCart = new Cart();             // Shopping cart to store items
        Scanner input = new Scanner(System.in);     // Retrieving user input

        int selection;

        do {
            printMenu();
            System.out.print("\nEnter your selection: ");
            selection = input.nextInt();
            if (selection < 0 || selection > 3) {
                System.out.println("Invalid Selection. Please select a choice from the given options.");
            }

            switch (selection) {
                case 1:
                    String itemName;
                    double itemPrice;
                    System.out.println("Enter a name for the item: ");
                    itemName = input.nextLine();
                    System.out.println("Enter the item price: ");
                    itemPrice = input.nextDouble();

                    shoppingCart.addItem(new Item(itemName, itemPrice));
                    break;
                case 2:
                    Item[] items = shoppingCart.returnCart();
                    if (items.length == 0) {
                        System.out.println("Shopping Cart is Empty!");
                    } else {
                        for (Item item: shoppingCart.returnCart()) {
                            System.out.printf("Name: %s Price: %f", item.getName(), item.getPrice());
                        }
                    }
                case 3:
                    System.out.println("CHECKING OUT ITEMS...");
                    double totalPrice = 0;
                    for (Item item : shoppingCart.returnCart()) {
                        System.out.println(item);
                        totalPrice += item.getPrice();
                    }
                    System.out.printf("\n\nFINAL PRICE: %f", totalPrice);
                    break;
                case 0:
                    System.out.println("STOPPING PROGRAM");
                    break;
            }
        }
        while (selection != 0);
    }
}