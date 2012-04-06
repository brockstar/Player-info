import sqlite3


def write_image(data):
    try:
        f = open('temp.jpg', 'wb')
        f.write(data)
    except IOError, e:
        print 'Error %d: %s' % (e.args[0], e.args[1])
        
def get_player_image(player_name):
    success = False
    try:
        con = sqlite3.connect('test.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('select Image from Players where Name="%s"' % (player_name))
        data = cur.fetchall()
        con.close()
        success = True
        write_image(data['Image'])
    except:
        pass
    return success