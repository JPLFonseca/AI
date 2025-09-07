package maqest;

import java.util.HashMap;


public class Estado<EV,AC> {

    // vao ser iniciadas as variaveis nome, estadoSucessor e transicoes
    private String nome;
    // private Transicao<EV,AC> estadoSucessor;
    private HashMap<EV, Transicao<EV,AC>> transicoes;

    public Estado(String nome){ // o construtor vai atribuir a variavel nome, o nome do estado e vai criar o dicionario com as transicoes
        this.nome = nome;
        transicoes = new HashMap<EV,Transicao<EV,AC>>();
    }

    public String getNome(){ // vai retornar o nome do estado
        return this.nome;
    }    

    public Transicao <EV,AC> processar(EV evento){ // vai fazer uma transicao de acordo com o evento
        Transicao<EV,AC> trans = transicoes.get(evento);
        return trans;
    }

    public Estado <EV,AC> transicao(EV evento, Estado <EV,AC> estadoSucessor){ 
        return transicao(evento,estadoSucessor, null);
    }

    public Estado <EV,AC> transicao(EV evento,Estado <EV,AC> estadoSucessor,AC accao){
        transicoes.put(evento,new Transicao<EV,AC>(estadoSucessor,accao));
        return this;
    }
    
}
