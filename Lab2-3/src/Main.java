import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Vector;

public class Main {
    public static void main(String[] args) {
        Problem problem = new Problem();
        Husband h1=new Husband("h1");
        Wife w1=new Wife("w1");
        Couple c1=new Couple(h1,w1);
        Husband h2=new Husband("h2");
        Wife w2=new Wife("w2");
        Couple c2=new Couple(h2,w2);
        Vector<Couple> couples = new Vector<Couple>(); // Presupunem ca vectorul de cupluri este initializat (Vector<Couple>  couples)
        couples.add(c1);
        couples.add(c2);
//        System.out.println(couples.get(0).toString());
//        System.out.println(couples.indexOf(c2));
//        Map<Integer,String>movedPersons=new HashMap<>();
//        movedPersons.put(1,"h");
//        movedPersons.put(1,"w");
//        for (Map.Entry<Integer,String> entry : movedPersons.entrySet()) {
//            System.out.println(entry.getKey() + ":" + entry.getValue());
//        }
        //State state= problem.initializare(couples);
    }
}
