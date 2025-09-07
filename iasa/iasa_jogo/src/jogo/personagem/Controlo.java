package jogo.personagem;

import maqest.MaquinaEstados;
import maqest.Estado;
import jogo.ambiente.Evento;


public class Controlo{

    private MaquinaEstados<Evento,Accao> maqEst; 

    public Controlo(){ // o construtor vai inicializar um novo estado. Neste contrutor vao ser definidos as transicoes entre estados.
        

        Estado<Evento,Accao> procura = new Estado<>("Procura");
        Estado<Evento,Accao> inspeccao = new Estado<>("Inspecção");
        Estado<Evento,Accao> observacao = new Estado<>("Observação");
        Estado<Evento,Accao> registo = new Estado<>("Registo");

        procura.transicao(Evento.ANIMAL,observacao,Accao.APROXIMAR).transicao(Evento.RUIDO,inspeccao,Accao.APROXIMAR).transicao(Evento.SILENCIO,procura,Accao.PROCURAR);

        inspeccao.transicao(Evento.ANIMAL, observacao,Accao.APROXIMAR).transicao(Evento.RUIDO,inspeccao,Accao.PROCURAR).transicao(Evento.SILENCIO,procura);

        observacao.transicao(Evento.ANIMAL,registo,Accao.OBSERVAR).transicao(Evento.FUGA,inspeccao);

        registo.transicao(Evento.FOTOGRAFIA,procura).transicao(Evento.FUGA,procura).transicao(Evento.ANIMAL,registo,Accao.FOTOGRAFAR);

        maqEst = new MaquinaEstados<>(procura);

    }

    public Estado <Evento,Accao> getEstado(){ // retorna o estado da maquina de estado
        return maqEst.getEstado();
    }

    public Accao processar(Percepcao percepcao){ // vai gerar uma resposta de acordo com a percepcao
        
        Accao action = maqEst.processar(percepcao.getEvento());
        mostrar();

        return action;
    }

    private void mostrar(){ // vai mostrar na consola
        System.out.println("Estado -> " + getEstado().getNome()); // deve mostrar a acao suponho eu
    }

}