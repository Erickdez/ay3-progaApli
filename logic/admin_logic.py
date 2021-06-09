from core.pyba_logic import PybaLogic


class AdminLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertAdmin(self, email, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `panpanbd`.`admins` "
            + "(`id_admin`,`email`,`password`,`salt`)"
            + f"VALUES(0,'{email}','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAdminByEmail(self, email):
        database = self.createDatabaseObj()
        sql = (
            "SELECT email, name, password, salt "
            + f"FROM panpanbd.admins where email like '{email}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
