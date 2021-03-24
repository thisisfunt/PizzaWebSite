from MainApp.models import product as productDB

def GetAllProducts():
    """return all info about all pizza"""
    q = productDB.objects.all()
    return q