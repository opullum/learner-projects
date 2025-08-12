/**
 * Cart (Class)
 * Meant to hold basic items. Items will be sorted into an array containing Items
 * @author Octavian Pullum
 * @version 1.0
 * @since 1.0
 */

import java.util.ArrayList;

public class Cart {
    ArrayList<Item> items = new ArrayList<>();

    public Item[] returnCart() {
        return items.toArray(new Item[0]);
    }

    public void addItem(Item newItem) {
        items.add(newItem);
    }

}