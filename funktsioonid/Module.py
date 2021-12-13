def Pindala(külg1:float,külg2:float)->float:
    """Riistküliku pindala leidmine
    :param float külg1:Riistküliku esimene külg
    :param float külg2:Riistküliku teine külg
    :rtype:float
    """
    S=külg1*külg2
    return S
def arithmetic(a:float,b:float,c:str):
    """Saab teha +,-,*,/ ja tagastab arv, kui vastus on arv ja "Tundamatu tehe", kui ei saa vastus leida.
    :param float a:esimene arv
    :param float b:teine arv
    :param str c:aritmeetilisa tehe
    :rtype:var
    """
    if c=="+":
        vastus=a+b
    elif c=="-":
        vastus=a-b
    elif c=="*":
        vastus=a*b
    elif c=="/":
        if b==0:
            vastus="на ноль делить нельзя"
        else:
            vastus=a/b
    else:
        print("Неизвестная операция")
    return vastus
def  is_year_leap(y:int)->int:
    """Visokosnii god ili net
    :param int y:year
    :rtype:float
    """
    if y%4:
        return True
    else:
        return False
def  square(a:int):
    """
    :param int a:storona kvadrata
    :rtype:int
    """
    P=(a+b)/2
    S=a*b

    
    
    return 