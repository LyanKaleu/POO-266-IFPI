from ConsultaMedica import ConsultaMedica
from relatorios import encontrar_consulta_por_paciente, relatorio_consultas_por_medico, relatorio_faturamento_clinica


def menu():
    consultas = []
    while True:
        print("\nMenu principal:")
        print("1 - Nova consulta (agendamento)")
        print("2 - Pagar consulta")
        print("3 - Cancelar consulta")
        print("4 - Agendar retorno")
        print("5 - Relatório de consultas realizadas no mês por médico")
        print("6 - Relatório de faturamento da clínica por mês")
        print("0 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            data_consulta = input("Data da consulta (dd/mm/aaaa): ")
            paciente = input("Nome do paciente: ")
            medico = input("Nome do médico: ")

            try:
                consulta = ConsultaMedica(data_consulta, paciente, medico)
                consultas.append(consulta)
                print(f"Consulta agendada com sucesso para o dia {consulta.data_consulta.strftime("%d/%m/%Y")}.")
            except ValueError as e:
                print(f"Erro ao agendar consulta: {e}")

        elif opcao == 2:
            paciente = input("Nome do paciente: ")
            consulta = encontrar_consulta_por_paciente(consultas, paciente)
            if consulta:
                try:
                    consulta.pago = True
                    print("Consulta paga com sucesso.")
                except ValueError as e:
                    print(f"Erro ao pagar consulta: {e}")
            else:
                print("Consulta não encontrada!")

        elif opcao == 3:
            paciente = input("Nome do paciente: ")
            consulta = encontrar_consulta_por_paciente(consultas, paciente)
            if consulta:
                try:
                    consulta.cancelado = True
                    consultas.remove(consulta)
                    print("Consulta cancelada com sucesso!")
                except ValueError as e:
                    print(f"Erro ao cancelar consulta: {e}")
            else:
                print("Consulta não encontrada!")

        elif opcao == 4:
            paciente = input("Nome do paciente: ")
            consulta = encontrar_consulta_por_paciente(consultas, paciente)
            if consulta:
                if consulta.pago:
                    data_retorno = input("Data do retorno (dd/mm/aaaa): ")
                    try:
                        consulta.data_retorno = data_retorno
                        print("Retorno agendado com sucesso!")
                    except ValueError as e:
                        print(f"Erro ao agendar retorno: {e}")
                else:
                    print("Consulta não paga, não pode agendar retorno!")
            else:
                print("Consulta não encontrada!")

        elif opcao == 5:
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (aaaa): "))
            relatorio = relatorio_consultas_por_medico(consultas, mes, ano)
            for medico, quantidade in relatorio.items():
                print(f"Médico: {medico}, Consultas: {quantidade}")

        elif opcao == 6:
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (aaaa): "))
            faturamento = relatorio_faturamento_clinica(consultas, mes, ano)
            print(f"Faturamento da clínica no mês {mes}/{ano}: R$ {faturamento}")

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")
