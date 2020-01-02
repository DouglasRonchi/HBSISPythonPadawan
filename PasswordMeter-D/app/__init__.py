from app.password.password import Password
from app.requirements.additions import Additions
from app.requirements.dedutions import Dedutions
from app.requirements.requirements import Requirements


def start():
    passwd = Password(input('Senha: '))
    add = Additions(passwd)
    ded = Dedutions(passwd)
    add.validate()
    ded.validate()
    add.show_score_total_points()
    add.show_addition_references()
    ded.show_dedution_references()
    return True
