from ConsultaMedica import ConsultaMedica
from collections import defaultdict


def relatorio_consultas_por_medico(consultas, mes, ano):
    consultas_por_medico = defaultdict(int)
    for consulta in consultas:
        if consulta.data_consulta.month == mes and consulta.data_consulta.year == ano:
            consultas_por_medico[consulta.medico] += 1
    return consultas_por_medico


def relatorio_faturamento_clinica(consultas, mes, ano):
    faturamento = 0
    for consulta in consultas:
        if (consulta.data_consulta.month == mes and consulta.data_consulta.year == ano) and consulta.pago:
            faturamento += ConsultaMedica.valor_consulta - ConsultaMedica.valor_medico
    return faturamento


def encontrar_consulta_por_paciente(consultas, nome_paciente):
    for consulta in consultas:
        if consulta.paciente == nome_paciente and not consulta.cancelado:
            return consulta
    return None
