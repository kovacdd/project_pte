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

        for time in range(start,end):

            cur.execute(sql,(time,))
            res = cur.fetchone()
            results.append(res)

        cur.close()
        conn.close()

        print(results)

        distance_km = (results[-1][2]*results[-1][3])/3600

        event = {
            "start": start,
            "end": end,
            "event_name": event_name,
            "duration": end - start,
            "KPI_1": distance_km,
            "KPI_2": None
        }

        print('Event: '+str(event))