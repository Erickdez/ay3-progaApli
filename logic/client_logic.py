from core.pyba_logic import PybaLogic


class ClientLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertClient(self, userName, userCel, userEmail, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `panpanbd`.`clients` "
            + "(`id_client`,`email`,`cel`,`name`,`password`,`salt`)"
            + f"VALUES(0,'{userEmail}','{userCel}','{userName}','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getClientByEmail(self, userEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT email, password, salt "
            + f"FROM panpanbd.clients where email like '{userEmail}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
