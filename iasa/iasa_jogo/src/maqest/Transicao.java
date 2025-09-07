package maqest;

public class Transicao<EV,AC> {

    private AC accao;
    private Estado<EV, AC> estadoSucessor;

    public Transicao(Estado <EV,AC> estadoSucessor, AC accao){ //este contrutor vai definir a accao e o estadoSucessor
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }
    
    public Estado <EV,AC> getEstadoSucessor(){ // vai retornar o estado sucessor
        return estadoSucessor;
    }

    public AC getAccao(){ // vai retornar a accao
        return this.accao;
    }
}
