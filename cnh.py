from datetime import datetime, timedelta


class CNH:
    sequencial = 0

    def __init__(self, nome, documento_identidade, cpf, data_nascimento,
                 filiacao, permissao, acc, categoria,
                 validade, primeira_habilitacao, data_emissao, observacoes=None):
        CNH.sequencial += 1
        self.numero = CNH.sequencial
        self.nome = nome
        self.documento_identidade = documento_identidade
        self.cpf = cpf
        self.validar_cpf()
        self.data_nascimento = self.validar_data(data_nascimento, "data de nascimento")
        self.filiacao = filiacao
        self.permissao = permissao
        self.acc = acc
        self.primeira_habilitacao = self.validar_data(primeira_habilitacao, "primeira habilitação")
        self.data_emissao = self.validar_data(data_emissao, "data de emissão")
        self.observacoes = observacoes
        self.validar_categoria(categoria)
        self.validade = self.validar_data(validade, "validade")

    def validar_cpf(self):
        if not self.cpf.isdigit() or len(self.cpf) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")

    def validar_idade(self):
        idade_minima = 18
        data_atual = datetime.now()
        if (data_atual - self.data_nascimento).days < idade_minima * 365:
            raise ValueError("Idade mínima para dirigir não alcançada.")

    def validar_categoria(self, categoria):
        categorias_validas = {
            "A": 0, "B": 1, "ACC": 2, "C": 3, "D": 4, "E": 5
        }

        requisitos_categorias = {
            "A": {"idade_minima": 18, "experiencia_minima": timedelta(days=0)},
            "B": {},
            "C": {"idade_minima": 19, "experiencia_minima": timedelta(days=365)},
            "D": {"idade_minima": 21, "experiencia_minima": timedelta(days=365 * 2)},
            "E": {"idade_minima": 21, "experiencia_minima": timedelta(days=365)}
        }

        for cat in categoria:
            if cat in categorias_validas:
                if cat in requisitos_categorias:
                    requisitos = requisitos_categorias[cat]
                    if requisitos.get("experiencia_minima") is not None and (
                            datetime.now() - self.primeira_habilitacao).days < requisitos["experiencia_minima"].days:
                        raise ValueError(
                            f"Para categoria {cat}, é necessário ter pelo menos "
                            f"{requisitos['experiencia_minima'].days / 365} anos de habilitação.")
                    if cat == "C" or cat == "D" or cat == "E":
                        if (datetime.now() - self.data_nascimento).days < requisitos["idade_minima"] * 365:
                            raise ValueError(f"Idade mínima de {requisitos['idade_minima']} anos para categoria {cat}")
                else:
                    raise ValueError(f"Não há exigências cadastradas para a categoria {cat}.")
            else:
                raise ValueError(f"Categoria inválida: {cat}")
        self.categoria = categoria

    def renovar_cnh(self, nova_validade):
        if self.verificar_renovacao():
            self.validade = self.validar_data(nova_validade, "validade")
        else:
            raise ValueError("A CNH ainda está válida. Renovação não permitida.")

    def validar_validade(self):
        if (self.validade - self.data_emissao).days < 0:
            raise ValueError("Data de validade da CNH deve ser posterior à data de emissão.")

    def verificar_renovacao(self):
        data_atual = datetime.now()
        if (self.validade - data_atual).days < 0:
            print("Sua CNH está vencida!")
        else:
            print("Sua CNH está válida!")

    @staticmethod
    def validar_data(data, nome_campo):
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            raise ValueError(f"Formato inválido para {nome_campo}. O formato correto é DD/MM/AAAA")

    def valida_vencimento(self, data):
        d = self.validar_data(data, "data de vencimento")
        if d.date() > datetime.now().date():
            return d
        else:
            raise ValueError("Data de vencimento inválida!")

    def __str__(self):
        return (f"Número do registro: {self.numero}"
                f"\nNome: {self.nome}"
                f"\nDocumento de Identidade: {self.documento_identidade}"
                f"\nCPF: {self.cpf}"
                f"\nData de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}"
                f"\nFiliação: {self.filiacao}"
                f"\nPermissão: {'Sim' if self.permissao else 'Não'}"
                f"\nACC: {'Sim' if self.acc else 'Não'}"
                f"\nCategoria: {', '.join(self.categoria)}"
                f"\nValidade: {self.validade.strftime('%d/%m/%Y')}"
                f"\nPrimeira Habilitação: {self.primeira_habilitacao.strftime('%d/%m/%Y')}"
                f"\nData de Emissão: {self.data_emissao.strftime('%d/%m/%Y')}"
                f"\nObservações: {self.observacoes if self.observacoes else 'Nenhuma'}")


def main():
    cnh1 = CNH("Lyan Kaleu", "1234567", "02819874320", "01/11/2004",
               "Maria José Meneses de Sousa Rocha e Luis Meneses de Santana",
               True, False, ['A', 'B'], "15/03/2024",
               "16/03/2023", "16/03/2023")
    cnh1.verificar_renovacao()

    cnh2 = CNH("João da Silva", "7654321", "12345678901", "07/05/1990",
               "Josué Samuel Silva Filho e Francisca Maria Portela Silva", True, True, ['D'],
               "08/10/2026", "08/11/2010", "01/11/2019", "Portador de necessidades especiais")
    cnh2.verificar_renovacao()

    try:
        cnh1.renovar_cnh("20/01/2027")
    except ValueError as e:
        print(f"Erro ao renovar a CNH: {e}")

    try:
        cnh1.validar_validade()
    except ValueError as e:
        print(f"Erro ao validar o vencimento da CNH: {e}")

    try:
        cnh2.validar_validade()
    except ValueError as e:
        print(f"Erro ao validar o vencimento da CNH: {e}")

    print("\nInformações sobre a CNH 1:")
    print(cnh1)

    print("\nInformações sobre a CNH 2:")
    print(cnh2)


if __name__ == '__main__':
    main()
