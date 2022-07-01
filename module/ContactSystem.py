from abc import ABC, abstractmethod

class ContactSystem(ABC):
    """Classe abstraite utilisée pour envoyer un message à un utilisateur."""

    @abstractmethod
    def send(self, message):
        """Toutes les sous-classes de ContactSystem doivent implémenter send."""
        pass


class TextContactSystem(ContactSystem):
    """Envoi un message à l'utilisateur par SMS."""

    def __init__(self, phone_number):
        """Initialise le numéro de téléphone."""
        super().__init__()
        validate_phone(phone_number)
        self.phone_number = phone_number

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" au numéro {self.phone_number}')

    def __str__(self):
        """Représentation lisible."""
        return f"Le numéro de téléphone est {self.phone_number}"


class OwlContactSystem(ContactSystem):
    """Envoi un message en utilisant une chouette ! 🧙‍♂️"""

    def __init__(self, address):
        """Initialise l'addresse."""
        varify_address(address)
        self.address = address
        self.owl = "Hedwige"
        super().__init__()

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" par chouette {self.owl}')

    def __str__(self):
        """Représentation."""
        return f"L'addresse est '{self.address}'"


def varify_address(address):
    """Fausse fonction qui retourne True."""
    return True


def validate_phone(phone_number):
    """Retourne True par défaut."""
    return True


def send_mass_messages(message, user_list):
    """Envoi des messages en masse.

    Utilise la méthode de message de chaque utilisateur."""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)
        
   
if __name__ == "main":
  send_mass_messages()