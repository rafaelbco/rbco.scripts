#!/usr/bin/python
#coding=utf8

from datetime import datetime

PARCELA = 653.92
DATA_ADIANTAMENTO = datetime(year=2010, month=6, day=14).date()
PARCELA_ANTECIPADA = 436.23
DATA_VENCIMENTO = datetime(year=2012, month=11, day=18).date()

def taxa_total_para_taxa_periodo(taxa_total, numero_de_periodos):
    return ((1 + taxa_total) ** (1. / numero_de_periodos)) - 1

def calc_parcela_antecipada(parcela, taxa_por_periodo, periodos_antecipados):
    return parcela * ((1 - taxa_por_periodo)**periodos_antecipados)

def investimento(valor, num_periodos, taxa_por_periodo):
    return valor * (1 + taxa_por_periodo)**num_periodos

def pagamento_multiplas_parcelas(
    valor_disponivel,
    valor_parcela_cheia,
    taxa_por_periodo,
    invest_func,
    num_periodos_ate_a_primeira_parcela=1):
    """

    """

def main():
    dias_antecipados = float((DATA_VENCIMENTO - DATA_ADIANTAMENTO).days)
    taxa_total =  (PARCELA - PARCELA_ANTECIPADA) / PARCELA_ANTECIPADA
    taxa_diaria = taxa_total_para_taxa_periodo(taxa_total, dias_antecipados)
    taxa_mensal = taxa_total_para_taxa_periodo(taxa_total, dias_antecipados / 30)
    parcela_antecipada = calc_parcela_antecipada(PARCELA, taxa_diaria, dias_antecipados)
    parcela_total = parcela_antecipada * (1 + taxa_diaria)**dias_antecipados

    print 'Valor da parcela: %s' % PARCELA
    print 'Valor da parcela com vencimento em %s adiantada em %s: %s' % (DATA_VENCIMENTO, DATA_ADIANTAMENTO, PARCELA_ANTECIPADA)
    print
    print 'A partir desses dados deriva-se as taxas:'
    print
    print 'Taxa total: %s %%' % (taxa_total * 100)
    print 'Taxa mensal: %s %%' % (taxa_mensal * 100)
    print 'Taxa diaria: %s %%' % (taxa_diaria * 100)
    print
    print 'Agora pode-se calcular de volta:'
    print
    print 'Parcela antecipada: %s (diferença %s)' % (parcela_antecipada, PARCELA_ANTECIPADA - parcela_antecipada)
    print 'Parcela total: %s (diferença %s)' % (parcela_total, PARCELA - parcela_total)
    print
    print 'Bônus:'
    print 'Taxa poupança por ano:', (1.005**12 - 1)

if __name__ == '__main__':
    main()

