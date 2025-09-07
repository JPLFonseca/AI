package jogo.ambiente;

import java.util.Scanner;
import java.util.HashMap;

public class Ambiente{

    private Evento evento;
	private HashMap<String,Evento> eventos;
    private Scanner scan = new Scanner(System.in);

    public Ambiente(){

        eventos = new HashMap<String,Evento>(); // no metodo Ambiente() vai ser criado um dicionario. Neste dicionario, vao ser atribuidas determinadas teclas a cada evento
        eventos.put("s",Evento.SILENCIO);
        eventos.put("r",Evento.RUIDO);
        eventos.put("a",Evento.ANIMAL);
        eventos.put("f",Evento.FUGA);
        eventos.put("o",Evento.FOTOGRAFIA);
        eventos.put("t",Evento.TERMINAR);

    }

    public Evento getEvento(){
        return evento;
    }

    public void evoluir(){ // este metodo vai gerar um novo evento e vai mostra-lo na consola atraves do metodo mostrar()

        this.gerarEvento();
        this.mostrar();
    }

    private Evento gerarEvento(){

        System.out.println("Escolher evento: ");
        String ev = scan.next();

        return eventos.get(ev);
    }

    private void mostrar(){
        System.out.println("Evento -> " + evento);
    }
}