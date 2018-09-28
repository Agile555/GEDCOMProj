#Mark Freeman

#just a utility to reset the database if it gets freaky
def reset_db(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS INDI")
    c.execute("DROP TABLE IF EXISTS FAM")
    c.execute("DROP TABLE IF EXISTS CHLD")

    c.execute("CREATE TABLE INDI(ID TEXT PRIMARY KEY, Name TEXT, Gender TEXT, Birthday TEXT, Age TEXT, Alive TEXT, Death TEXT, Child TEXT, Spouse TEXT)")
    c.execute("CREATE TABLE FAM(ID TEXT PRIMARY KEY, Married TEXT, Divorced TEXT, 'Husband ID' TEXT, 'Husband Name' TEXT, 'Wife ID' TEXT, 'Wife Name' TEXT, Children TEXT)")
    c.execute("CREATE TABLE CHLD(FAM_ID TEXT, INDI_ID TEXT)")

    conn.commit()