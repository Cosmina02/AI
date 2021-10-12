
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;


public class Problem {
    Vector<Couple> couples;
    State state = new State();
    // Map<Integer,String>movedPersons=new HashMap<>() ;

    // Daca se doreste aflarea nr-lui de sotii si soti de pe malul drept se va face o scadere (nr de cupluri - nr soti/sotii mal stang)
    public State initializare(Vector<Couple> couples) {
        // initializeaza cuplurile problemei si seteaza noua stare (0,nrCupluri,nrCupluri)
        this.couples = couples;
        state.setNewState(0, couples.size(), couples.size());
        return state;
    }

    public boolean checkFinalState() {
        // verifica daca toate cuplurile sunt pe malul drept si de asemenea daca si barca se afla tot pe malul drept
        if (state.nrOfWives == 0 && state.nrOfHusbands == 0 && state.side == 1) return true;
        return false;
    }

    private void newTransition(Map<Integer, String> movedPersons, int side) {
        if (side == 1) {
            for (Map.Entry<Integer, String> entry : movedPersons.entrySet()) {
                if (entry.getValue().contains("hw"))//daca se duce un cuplu
                {
                    couples.get(entry.getKey()).h.side = 1;
                    couples.get(entry.getKey()).w.side = 1;
                    state.nrOfWives--;
                    state.nrOfHusbands--;
                    break;
                }
                if (entry.getValue().contains("w")) {
                    couples.get(entry.getKey()).w.side = 1;
                    state.nrOfWives--;
                } else {
                    couples.get(entry.getKey()).h.side = 1;
                    state.nrOfHusbands--;
                }

            }
        } else {
            for (Map.Entry<Integer, String> entry : movedPersons.entrySet()) {
                if (entry.getValue().contains("hw"))//daca se duce un cuplu
                {
                    couples.get(entry.getKey()).h.side = 0;
                    couples.get(entry.getKey()).w.side = 0;
                    state.nrOfWives++;
                    state.nrOfHusbands++;
                    break;
                }
                if (entry.getValue().contains("w")) {
                    couples.get(entry.getKey()).w.side = 0;
                    state.nrOfWives++;
                } else {
                    couples.get(entry.getKey()).h.side = 0;
                    state.nrOfHusbands++;
                }
            }
        }
    }

    private boolean safeTransition(Map<Integer, String> movedPersons, int side) {
       //de verificat daca fiecare sotie are sotul ei pe mal
        newTransition(movedPersons, side);
        int leftH = state.nrOfHusbands;
        int leftW = state.nrOfWives;
        int rightH = couples.size() - state.nrOfHusbands;
        int rightW = couples.size() - state.nrOfWives;
        if (leftH < 0 || leftW < 0 || rightH < 0 || rightW < 0) {
            newTransition(movedPersons, (side + 1) % 2);
            return false;
        } else if (leftW != 0 && leftW < leftH) {
            newTransition(movedPersons, (side + 1) % 2);
            return false;
        } else if (rightW != 0 && rightW < rightH) {
            newTransition(movedPersons, (side + 1) % 2);
            return false;
        } else {
            newTransition(movedPersons, (side + 1) % 2);
            return true;
        }
    }

    private boolean backtraking(String prevTransition){
        if(checkFinalState()){
            System.out.println("Solved!\n");
            return true;
        }else{
            for(int i=0;i<couples.size();i++){
                for(int k=0;k<2;k++){
                    if(k==0){
                        Husband H1=couples.get(i).h;
                        for(int j=0;j<couples.size();j++){
                            for(int t=0;t<2;t++){
                                if(t==0){
                                    Husband H2=couples.get(j).h;
                                    if(H1.equals(H2)){
                                        continue;
                                    }else{
                                        Map<Integer,String>movedPersons=new HashMap<>();
                                        movedPersons.put(i,"h");
                                        movedPersons.put(j,"h");
                                        if(safeTransition(movedPersons,state.side)){
                                            newTransition(movedPersons,state.side);
                                            state.side=(state.side+1)%2;
                                            t=2;
                                            j=couples.size();
                                            k=2;

                                        }
                                    }
                                }
                            }

                            Wife W2=couples.get(j).w;

                        }
                    }

                    Wife W1=couples.get(i).w;

                }

            }
        }

        return false;
    }


}
