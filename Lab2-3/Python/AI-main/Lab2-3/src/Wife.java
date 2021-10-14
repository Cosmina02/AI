public class Wife {
    public int side=0;
    public String name;

    public Wife(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Wife{" +
                "side=" + side +
                ", name='" + name + '\'' +
                '}';
    }
}
