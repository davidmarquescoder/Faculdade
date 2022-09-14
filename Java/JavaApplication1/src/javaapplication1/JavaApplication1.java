package javaapplication1;
public class JavaApplication1 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.cor = "azul";
        c1.ponta = 0.5f;
        c1.modelo = "bic";
        c1.tampar();
        c1.carga = 50;
        c1.status();
        c1.rabiscar();
        
        Caneta c2 = new Caneta();
        c2.cor = "vermelha";
        c2.ponta = 0.7f;
        c2.modelo = "bic";
        c2.destampar();
        c2.carga = 80;
        c2.status();
        c2.rabiscar();
    }
}
