package jogo;

import jogo.ambiente.Ambiente;
import jogo.personagem.Personagem;
import jogo.ambiente.Evento;

public class Jogo{

    private static Ambiente ambiente;
    private static Personagem personagem;

public static void main(String[] args){

    // neste metodo sao inicializadas as variaveis ambiente e personagem. Estas variaveis, vao, respetivamente, criar um ambiente e uma personagem. Apos a criacao das variaveis, vai ser executado o metodo executar() 

    ambiente = new Ambiente();
    personagem = new Personagem(ambiente);
    executar();
}

private static void executar(){ // neste metodo vai ser executado o metodo executar da classe Personagem e, seguidamente, vai evoluir o ambiente, sendo assim criado o jogo. Apos a evolucao do ambiente, vai atribuir o valor do evento do ambiente atual a uma variavel evento e vai ser verificada a condicao, se o jogo ja terminou ou nao
    Evento evento;

   do{

        personagem.executar();
        ambiente.evoluir();
        evento = ambiente.getEvento();
        
    }while((evento != Evento.TERMINAR));
}}