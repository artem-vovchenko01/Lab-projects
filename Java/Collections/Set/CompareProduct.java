import java.util.Comparator;

    public class CompareProduct implements Comparator<Product> {
        @Override
        public int compare (Product p1, Product p2) {
            return p1.getRecommendedPrice() - p2.getRecommendedPrice();
        }
    }
