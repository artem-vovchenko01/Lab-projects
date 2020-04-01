import java.util.List;
import java.util.LinkedList;
import java.util.TreeSet;
import java.util.Set;

public class Shop implements ShopInterface, Comparable<Shop> {
    private String title;
    private Set<String> products = new TreeSet();

    public Shop(String title) {
        if (title.length() == 0) {
            throw new IllegalArgumentException("Назва не може бути порожньою. ");
        }
        this.title = title;
        Database.registerShop(this);
    }
    @Override
    public void addProduct(Product product, int price) {
        if (price <= 0) {
            throw new IllegalArgumentException("Ціна має бути більшою від 0. ");
        }
        products.add(product.toString() + ":" +  price);
        product.addShop(this);
    }
    @Override
    public int getPrice(Product product) { ;
        String price_this = "";
        for (String prod : products) {
            if (prod.split(":")[0].equals(product.toString())) {
                price_this = prod.split(":")[1];
            }
        }
        if (price_this.equals("")) {
            throw new IllegalArgumentException("У магазині немає даного товару. ");
        }
        return Integer.valueOf(price_this);
    }

    public Set<Product> getProducts() {
        Set<Product> to_return = new TreeSet(new CompareProduct());
        Database DB = new Database();
        for (Product prod : Database.getProducts()) {
            for (String our_prod : products) {
                if (prod.toString().equals(our_prod.split(":")[0])) {
                    to_return.add(prod);
                }
            }
        }
        return to_return;
    }
    public Set<String> getProductsWithPrices () {
        return products;
    }
    @Override
    public String toString() {
        return title;
    }

    @Override
    public int compareTo(Shop other) {
        return this.title.compareTo(other.title);
    }
}
