public class Husband {
    public int side=0;
    public String name;

    public Husband(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Husband{" +
                "side=" + side +
                ", name='" + name + '\'' +
                '}';
    }
}
