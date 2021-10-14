public class State {
    /*Starea va fi reprezentata astfel:
    side = 0 reprezinta partea stanga a malului, iar 1 reprezinta partea dreapta a malului unde se afla barca;
    nrOfWives = nr de sotii de pe malul stang
    nrOfHusbands = nr de soti de pe malul stang
     */
    public int side=0;

    public int nrOfWives;
    public int nrOfHusbands;

    public void setNewState(int newSide, int nrWives, int nrHusbands){
        side=newSide;
        nrOfWives=nrWives;
        nrOfHusbands= nrHusbands;
    }
}
