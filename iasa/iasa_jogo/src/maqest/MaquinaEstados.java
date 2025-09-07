package maqest;

public class MaquinaEstados <EV,AC>{

    private Estado <EV,AC> estado;

public MaquinaEstados(Estado <EV,AC> estado){ // este construtor vai receber um estado e vai guarda-lo na variavel estado
    this.estado = estado;
}

public Estado <EV,AC> getEstado(){ // retorna a variavel estado com o valor do estado atual
    return this.estado;
}

public AC processar(EV evento){ // vai processar o evento recebido e verifica se este nao e null. Se for null, retorna null, caso contrario vai buscar o estado sucessor e vai retornar a accao
    Transicao<EV,AC> transicao = estado.processar(evento);
    if(transicao != null){

        estado = transicao.getEstadoSucessor();
        return transicao.getAccao();
    } else {

    return null;}
}
}