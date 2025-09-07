package jogo.personagem;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;

public class Personagem{

    private Controlo controlo;
    private Ambiente ambiente;
    private Percepcao percepcao;


    // neste metodo e iniciado a personagem no ambiente definido. E iniciado a variavel controlo e a variavel ambiente
    public Personagem(Ambiente ambiente){
        
        controlo = new Controlo();
        this.ambiente = ambiente;
    }

    public void executar(){ // neste metodo vai chamar-se o metodo percepcionar, que ira retornar uma percecao. Esta percecao ira ser enviada para o controlo que a ira processar e ira retornar uma accao, que vai ser enviada para o metodo actuar. O comportamento sera gerado com base em associacoes entre estimulos, as percepcoes, e respostas, as acoes.
        percepcao = this.percepcionar();
        actuar(controlo.processar(percepcao));
    }

    private Percepcao percepcionar(){ // este metodo vai buscar o evento atual do ambiente e a partir desse evento vai gerar uma percecao e retorna-la

        Evento evento = ambiente.getEvento();
        Percepcao percepcao = new Percepcao(evento);

        return percepcao;
    }

    private void actuar(Accao accao){ // este metodo vai executar a accao que foi previamente retornada pelo controlo apos processar a percecao

        if(accao != null)
        System.out.println("Accao -> " + accao);
    }



}