from django.db import models
from django.conf import settings

# Define a classe Room que representa uma sala de bate-papo.
class Room(models.Model):
    # Relaciona a sala a um usuário específico (proprietário da sala).
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário padrão configurado no Django.
        on_delete=models.CASCADE,  # Remove a sala caso o usuário associado seja deletado.
    )
    # Define o título da sala como um campo de texto com limite de 200 caracteres.
    title = models.CharField(max_length=200)
    # Estabelece uma relação muitos-para-muitos entre a sala e as mensagens.
    messages = models.ManyToManyField('Message')
    # Armazena a data e a hora de criação da sala (preenchido automaticamente ao criar).
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

    
# Define a classe Message que representa uma mensagem no sistema.
class Message(models.Model):
    # Relaciona a mensagem a um usuário específico (autor da mensagem).
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário padrão configurado no Django.
        on_delete=models.CASCADE,  # Remove a mensagem caso o usuário associado seja deletado.
    )
    # Define o texto da mensagem como um campo de texto sem limite de comprimento.
    text = models.TextField()
    # Armazena a data e a hora de criação da mensagem (preenchido automaticamente ao criar).
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}: {self.text} {self.created_at}"
