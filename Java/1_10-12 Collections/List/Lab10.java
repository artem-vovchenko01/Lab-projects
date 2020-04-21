import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Lab10 {
    public static void main(String[] args) {
        Shop dobrunya = new Shop("Добриня");
        Shop silpo = new Shop("Сільпо");
        Shop atb = new Shop("АТБ");
        Shop fora = new Shop("Фора");

        Product water = new Product("Вода", 15);
        Product bread = new Product("Хліб", 20);
        Product milk = new Product("Молоко", 28);
        Product chocolate = new Product("Шоколад", 40);

        dobrunya.addProduct(water, 14);
        silpo.addProduct(water, 16);
        atb.addProduct(water, 13);
        fora.addProduct(water, 13);

        dobrunya.addProduct(bread, 18);
        silpo.addProduct(bread, 20);
        atb.addProduct(bread, 19);
        fora.addProduct(bread, 20);

        dobrunya.addProduct(milk, 27);
        silpo.addProduct(milk, 30);
        atb.addProduct(milk, 25);

        silpo.addProduct(chocolate, 39);
        atb.addProduct(chocolate, 39);
        fora.addProduct(chocolate, 40);

        List<Product> products = new ArrayList<Product>();
        products.add(water); products.add(bread); products.add(milk);
        for (Product product : products) {
            System.out.println("Найменша ціна на " + product + ": " + product.findMinPrice());
            Iterator best_shops_iter = product.findBestShops().iterator();
            String best_shop_string = "";
            while (best_shops_iter.hasNext()) {
                Shop shop = (Shop) best_shops_iter.next();
                best_shop_string += shop.toString() + " ";
            }
            System.out.println("Товар " + product + " продається за найкращою ціною " + product.findMinPrice() + " в магазинах " + best_shop_string + "\n");
        }

        Searcher main_search = new Searcher();
        System.out.println("Магазини, в яких ціни менші, ніж рекомендовані: ");
        String cheapest_string = "";
        Iterator<Shop> cheapest_iter = main_search.isCheapestExists().iterator();
        while (cheapest_iter.hasNext()) {
            cheapest_string += cheapest_iter.next().toString() + " ";
        }
        if (cheapest_string.length() != 0) {
            System.out.println(cheapest_string);
        } else {
            System.out.println("Немає магазинів, у яких ціни менші за рекомендовані. ");
        }
    }
}
