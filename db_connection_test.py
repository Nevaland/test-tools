import telnetlib
import pymysql
from config import DB_CONFIGS


def is_right_acl(db_config):
    print("  [+] ACL Check")
    if _can_connect_with_telnet(db_config):
        return True
    else:
        return False


def _can_connect_with_telnet(db_config):
    try:
        telnetlib.Telnet(db_config['host'], port=db_config['port'], timeout=5)
        return True

    except Exception as ex:
        print("   [-] can't connect with telnet")
        print(ex)
        return False


def can_use_db(db_config):
    print("  [+] DB Check")
    try:
        conn = pymysql.connect(host=db_config['host'], port=db_config['port'],
                               user=db_config['user'], password=db_config['password'],
                               db=db_config['db'], charset='utf8mb4', use_unicode=True)

        if not _can_execute_sql(conn):
            return False

    except Exception as ex:
        print("   [-] Can't connect to MySQL server")
        print(ex)
        return False

    finally:
        conn.close()
        
    return True


def _can_execute_sql(conn):
    try:
        with conn.cursor() as curs:
            curs.execute("select version()")
            print("   [+] version: " + str(curs.fetchone()))
        return True

    except Exception as ex:
        print("   [-] Can't execute my SQL")
        print(ex)
        return False

if __name__ == '__main__':
    print("[*] DB Connection Check")

    i = 0
    for db_config in DB_CONFIGS:
        print(" [*] %d. %s (%s) - %s" % (i, db_config['host'], db_config['port'], db_config['db']))
        if is_right_acl(db_config) and can_use_db(db_config):
            print(" [+] Finished DB Connection Check (Success)")
        else:
            print(" [-] Finished DB Connection Check (Failed)")
