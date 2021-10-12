public class Couple {
    public Husband h;
    public Wife w;

    public Couple(Husband h, Wife w) {
        this.h = h;
        this.w = w;
    }
    //de construit cupluri in functie de nr dat

    @Override
    public String toString() {
        return "Couple{" +
                "h=" + h +
                ", w=" + w +
                '}';
    }
}
