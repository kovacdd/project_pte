import sqlite3

class SQLDatabase():

    def __init__(self, database):
        try:
            self.conn = sqlite3.connect(database, check_same_thread=False)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def is_table(self, name):
        sql = """
        SELECT name FROM sqlite_master WHERE type='table' AND name = ?
        """
        self.cur.execute(sql, (name,))
        return self.cur.fetchone()

    def drop_table(self):
        sql = """
        DROP TABLE data
        """
        self.cur.execute(sql)

    def create_table(self, name):
        sql = """
        CREATE TABLE data (ID INTEGER PRIMARY KEY AUTOINCREMENT, VEHICLE, TIME, SPEED, N, MD, NOX_EO, NOX_TP, T_OIL, T_W_I, T_W_O, MF_FUEL)
        """
        if not self.is_table(name):
            self.cur.execute(sql)

    def insert(self, values):
        sql = """
        INSERT INTO data (VEHICLE, TIME, SPEED, N, MD, NOX_EO, NOX_TP, T_OIL, T_W_I, T_W_O, MF_FUEL) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
        """

        vehicle = values[0]
        time = values[1]
        speed = values[2]
        n = values[3]
        md = values[4]
        nox_eo = values[5]
        nox_tp = values[6]
        t_oil = values[7]
        t_w_i = values[8]
        t_w_o = values[9]
        mf_fuel = values[10]

        self.cur.execute(sql, (vehicle, time, speed, n, md, nox_eo, nox_tp, t_oil, t_w_i, t_w_o, mf_fuel))
        self.conn.commit()

    def insert_all(self, data):
        for value in data:
            self.insert(value)

    def select(self):
        sql = """
        SELECT ID, VEHICLE, TIME, SPEED, N, MD, NOX_EO, NOX_TP, T_OIL, T_W_I, T_W_O, MF_FUEL FROM data
        """
        res = self.cur.execute(sql)
        return res.fetchall()
    
    def select_by_id(self, id):
        sql = """
        SELECT ID, VEHICLE, TIME, SPEED, N, MD, NOX_EO, NOX_TP, T_OIL, T_W_I, T_W_O, MF_FUEL FROM data WHERE ID
        """
        res = self.cur.execute(sql, (id,))
        return res.fetchall()
    
    def print(self):
        print(self.select())

    def close(self):
        self.cur.close()
        self.conn.close()