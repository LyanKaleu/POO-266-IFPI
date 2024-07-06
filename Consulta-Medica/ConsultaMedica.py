from datetime import datetime, date


class ConsultaMedica:
    valor_consulta = 300
    valor_medico = 200

    def __init__(self, data_consulta, paciente, medico, pago=False, cancelado=False):
        self.data_consulta = self.validar_data(data_consulta)
        self._data_retorno = None
        self.paciente = paciente
        self.medico = medico
        self._pago = pago
        self._cancelado = cancelado

    @staticmethod
    def validar_data(data_str):
        d = datetime.strptime(data_str, "%d/%m/%Y").date()
        if d <= date.today() or d.weekday() in [5, 6]:
            raise ValueError("Data inválida para consulta!")
        return d

    @property
    def data_retorno(self):
        return self._data_retorno

    @data_retorno.setter
    def data_retorno(self, data_retorno):
        retorno_data = datetime.strptime(data_retorno, "%d/%m/%Y").date()
        if not self._pago:
            raise ValueError("Consulta não paga, não pode agendar retorno!")
        if retorno_data <= self.data_consulta or (retorno_data - self.data_consulta).days > 30:
            raise ValueError("Data de retorno inválida!")
        self._data_retorno = retorno_data

    @property
    def pago(self):
        return self._pago

    @pago.setter
    def pago(self, valor):
        if self._cancelado:
            raise ValueError("Consulta cancelada, não pode ser paga!")
        self._pago = valor

    @property
    def cancelado(self):
        return self._cancelado

    @cancelado.setter
    def cancelado(self, valor):
        if self._pago:
            raise ValueError("Consulta já paga, não pode ser cancelada!")
        self._cancelado = valor
