/**
 * Item (Class)
 * Represents individual items. Meant to be used with class Cart.
 * Items contain a price and name. Retrievable through getter mthods.
 * @author Octavian Pullum
 * @version 1.0
 * @since 1.0
 */

public class Item {

    final private String name;
    final private double price;

    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        String ItemString = "%s (%f)";
        return String.format(ItemString, name, price);
    }
}
