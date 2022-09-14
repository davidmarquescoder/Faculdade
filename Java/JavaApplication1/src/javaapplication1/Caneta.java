package javaapplication1;

public class Caneta {
    String modelo;
    String cor;
    float ponta;
    int carga;
    boolean tampada;
    
    void status(){
        System.out.println("Cor: " + this.cor);
        System.out.println("Tampada: " + this.tampada);
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Carga: " + this.carga);
    }
    void rabiscar(){
        if(tampada == true){
            System.out.println("ERRO, Caneta tampada");
        }
        else{
            System.out.println("Estou rabiscando");
        }
    }
    void destampar(){
        this.tampada = false;
    }
    void tampar(){
        this.tampada = true;
    }
}
