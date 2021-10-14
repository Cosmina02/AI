
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
                if (entry.getValue().equals("hw"))//daca se duce un cuplu
                {
                    couples.get(entry.getKey()).h.side = 1;
                    couples.get(entry.getKey()).w.side = 1;
                    state.nrOfWives--;
                    state.nrOfHusbands--;
                    break;
                }
                if (entry.getValue().equals("w")) {
                    couples.get(entry.getKey()).w.side = 1;
                    state.nrOfWives--;
                } else {
                    couples.get(entry.getKey()).h.side = 1;
                    state.nrOfHusbands--;
                }

            }
        } else {
            for (Map.Entry<Integer, String> entry : movedPersons.entrySet()) {
                if (entry.getValue().equals("hw"))//daca se duce un cuplu
                {
                    couples.get(entry.getKey()).h.side = 0;
                    couples.get(entry.getKey()).w.side = 0;
                    state.nrOfWives++;
                    state.nrOfHusbands++;
                    break;
                }
                if (entry.getValue().equals("w")) {
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
        int rightH = couples.size() - state.nrOfHusbands + 1;
        int rightW = couples.size() - state.nrOfWives + 1;
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

    public boolean backtraking(int poz1, String p1, int poz2, String p2) {
        if (checkFinalState()) {
            System.out.println("Solved!\n");
            return true;
        } else {
            for (int i = 0; i < couples.size(); i++) {
                for (int k = 0; k < 2; k++) {
                    if (k == 0) { // daca s-a ales sotul ii cautam pereche
                        Husband H1 = couples.get(i).h;
                        for (int j = 0; j < couples.size(); j++) { // parcurgen vectorul de cupluri
                            for (int t = 0; t < 2; t++) { // alegem sotul sau sotie
                                if (t == 0) { // daca este sot
                                    Husband H2 = couples.get(j).h;
                                    if (H1.equals(H2)) { // sotul se duce singur
                                        Map<Integer, String> movedPersons = new HashMap<>();
                                        movedPersons.put(i, "h");
                                        if (safeTransition(movedPersons, state.side)) {
                                            newTransition(movedPersons, state.side);
                                            state.side = (state.side + 1) % 2;

                                            if (backtraking(i, "h", 0, "")) {
                                                System.out.println("In the boat: h"+i+" -1");
                                                return true;
                                            }
                                        }

                                    } else {
                                        Map<Integer, String> movedPersons = new HashMap<>();
                                        movedPersons.put(i, "h"); // primul sot
                                        movedPersons.put(j, "h"); // al2lea sot
                                        if (safeTransition(movedPersons, state.side)) {
                                            newTransition(movedPersons, state.side);
                                            state.side = (state.side + 1) % 2;

                                            if (backtraking(i, "h", j, "h")) {
                                                System.out.println("In the boat: h"+i+" h"+j);
                                                return true;
                                            }
                                        }
                                    }
                                } else { // daca se va duce impreuna cu o sotie
                                    Wife W2 = couples.get(j).w;

                                    Map<Integer, String> movedPersons = new HashMap<>();
                                    if (i == j) {
                                        movedPersons.put(i, "hw");
                                    } else {
                                        movedPersons.put(i, "h"); // primul sot
                                        movedPersons.put(j, "w"); // al2lea sot
                                    }
                                    if (safeTransition(movedPersons, state.side)) {
                                        newTransition(movedPersons, state.side);
                                        state.side = (state.side + 1) % 2;

                                        if (backtraking(i, "h", j, "w")) {
                                            System.out.println("In the boat: h"+i+" w"+j);
                                            return true;
                                        }
                                    }
                                }
                            }

                        }
                    }
                    if (k == 1) {
                        Wife W1 = couples.get(i).w;
                        for (int j = 0; j < couples.size(); j++) { // parcurgen vectorul de cupluri
                            for (int t = 0; t < 2; t++) {
                                if (t == 0) {
                                    Wife W2 = couples.get(j).w;

                                    if (W1.equals(W2)) { // sotul se duce singur
                                        Map<Integer, String> movedPersons = new HashMap<>();
                                        movedPersons.put(i, "w");

                                        if (safeTransition(movedPersons, state.side)) {
                                            newTransition(movedPersons, state.side);
                                            state.side = (state.side + 1) % 2;

                                            if (backtraking(i, "w", -1, "")) {
                                                System.out.println("In the boat: w"+i+" -1");
                                                return true;
                                            }
                                        }

                                    } else {
                                        Map<Integer, String> movedPersons = new HashMap<>();
                                        movedPersons.put(i, "w"); // primul sot
                                        movedPersons.put(j, "w"); // al2lea sot
                                        if (safeTransition(movedPersons, state.side)) {
                                            newTransition(movedPersons, state.side);
                                            state.side = (state.side + 1) % 2;

                                            if (backtraking(i, "w", j, "w")) {
                                                System.out.println("In the boat: w"+i+" w"+j);
                                                return true;
                                            }
                                        }
                                    }

                                } else {
                                    Wife W2 = couples.get(j).w;

                                    Map<Integer, String> movedPersons = new HashMap<>();
                                    if (i == j) {
                                        movedPersons.put(i, "hw");
                                    } else {
                                        movedPersons.put(i, "w"); // primul sot
                                        movedPersons.put(j, "h"); // al2lea sot
                                    }
                                    if (safeTransition(movedPersons, state.side)) {
                                        newTransition(movedPersons, state.side);
                                        state.side = (state.side + 1) % 2;

                                        if (backtraking(i, "w", j, "h")) {
                                            System.out.println("In the boat: w"+i+" h"+j);
                                            return true;
                                        }
                                    }
                                }

                            }
                        }
                    }

                }

            }
        }

        return false;
    }


}
