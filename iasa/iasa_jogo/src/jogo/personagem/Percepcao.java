package jogo.personagem;

import jogo.ambiente.Evento;

public class Percepcao{

    private Evento evento;

    public Percepcao(Evento evento){ // este metodo vai iniciar uma percepcao a partir de um evento
        this.evento = evento;
    }

    public Evento getEvento(){ // este metodo vai retornar o evento atual
        return this.evento;
    }
}