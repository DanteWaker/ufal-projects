class VectorClock:
    def __init__(self, process_id, num_processes):
        """
        Inicializa um novo relógio vetorial para um processo específico.

        :param process_id: O identificador único deste processo.
        :param num_processes: O número total de processos no sistema.
        """
        self.process_id = process_id
        self.vector = [0 for _ in range(num_processes)]
        
    def increment(self):
        """Incrementa o contador para o processo atual."""
        self.vector[self.process_id] += 1

    def update(self, received_vector):
        """Atualiza o vetor baseando-se no vetor recebido."""
        self.increment()  # Evento interno: incrementa antes de atualizar com o vetor recebido.
        for i in range(len(self.vector)):
            self.vector[i] = max(self.vector[i], received_vector[i])

    def __str__(self):
        """Retorna a representação em string do vetor."""
        return str(self.vector)

    def internal_event(self):
        """
        Registra um evento interno, incrementando o contador deste processo.
        """
        self.vector[self.process_id] += 1

    def send_event(self):
        """
        Prepara o relógio vetorial para ser enviado com uma mensagem, registrando um evento interno.
        
        :return: Uma cópia do relógio vetorial atual.
        """
        self.internal_event()
        return self.vector.copy()

    def receive_event(self, received_vector):
    # Atualiza cada posição do vetor com o máximo entre o valor atual e o recebido
      for i in range(len(self.vector)):
          self.vector[i] = max(self.vector[i], received_vector[i])
      # Incrementa a posição deste processo no vetor
      self.internal_event()

    def __repr__(self):
        """
        Retorna uma representação string do estado atual do relógio vetorial.
        """
        return f"VectorClock(process_id={self.process_id}, vector={self.vector})"
