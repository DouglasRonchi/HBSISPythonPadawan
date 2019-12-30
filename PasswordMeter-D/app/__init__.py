from app.password.password import Password
from app.requirements.additions import Additions
from app.requirements.dedutions import Dedutions
from app.requirements.requirements import Requirements


def start():
    passwd = Password(input("Senha: "))
    add = Additions(passwd)
    ded = Dedutions(passwd)
    add.validate()
    ded.validate()
    print(add.get_score_validated() - ded.get_score_validated())
