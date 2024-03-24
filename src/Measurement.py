import sqlite3

class Measurement():

    def __init__(self, database):
        self.database = database

    def event_detection(self, start, end, event_name):

        sql = """
        SELECT ID, VEHICLE, TIME, SPEED, N, MD, NOX_EO, NOX_TP, T_OIL, T_W_I, T_W_O, MF_FUEL FROM data WHERE ID=?
        """
        results = []

        conn = sqlite3.connect(self.database, check_same_thread=False)
        cur = conn.cursor()

        for id in range(1,10):

            cur.execute(sql,(id,))
            res = cur.fetchone()
            results.append(res)

        cur.close()
        conn.close()

        print(results)

        event = {
            "start": start,
            "end": end,
            "event_name": event_name,
            "duration": end - start,
            "KPI_1": None,
            "KPI_2": None
        }

        print(event)