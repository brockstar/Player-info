import re
import sqlite3


class PlayerLookup:
    def __init__(self, player_name, db_name='test.db'):
        self.con = sqlite3.connect(db_name)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.player = player_name
        if self.__player_exists(self.player):
            self.exists = True
        else:
            self.exists = False
            print 'Error: Player not found in database.'
        
    def __del__(self):
        self.con.close()
    
    def get_player_image(self):
        if self.exists:
            success = False
            try:
                self.cur.execute('select Image from Players where Name="%s"'
                                 % (self.player))
                data = self.cur.fetchone()
                success = True
                self.__write_image(data['Image'])
            except:
                print 'Error looking up player image.'
            return success
            
    def get_player_attributes(self, attr_dict):
        if self.exists:
            self.cur.execute('select * from Players where Name="%s"' 
                             % (self.player))
            attributes = self.cur.fetchone()
            d = {}
            for key in attr_dict:
                if not key in ['Stats', 'Image']:
                    try:
                        d[key] = attributes[key]
                    except IndexError:
                        print 'Warning: Key "%s" not found in database.' % key
            return d
        
    def get_player_stats(self, year):
        if self.exists:
            self.cur.execute('select Stats from Players where Name="%s"'
                             % (self.player))
            # Retrieve stats, cast as string and remove brackets.
            stats = self.cur.fetchone()['Stats']
            lines = []
            for line in stats.encode().split('\n'):
                lines += [line.split(',')]
            return lines[0][1:], lines[1][1:]
        
    def __player_exists(self, player_name):
        self.cur.execute('select distinct Name from Players')
        names = self.cur.fetchall()[0]
        if player_name in names:
            exists = True
        else:
            exists = False
        return exists
    
    def __write_image(self, data):
        try:
            f = open('temp.png', 'wb')
            f.write(data)
        except IOError, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])