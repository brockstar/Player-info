import re
import sqlite3


class PlayerLookup:
    '''
    This class returns the information for the given player from the 
    given database. Player image, player stats and player attributes 
    can be retrieved.
    '''
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
        '''
        Writes player profile image to temp.png and returns True on success
        and False on failure.
        '''
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
        '''
        Returns all attribues given in *attr_dict* from the database.
        For getting stats use **get_player_stats**, for getting player
        profile image use **get_player_image**.
        '''
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
        '''
        Returns the stats for the given years.
        CAUTION: At the moment it only returns the stat names and the
        stats from the last year found in the DB.
        '''
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
        '''
        Checks if player exists in database.
        '''
        self.cur.execute('select distinct Name from Players')
        names = self.cur.fetchall()[0]
        if player_name in names:
            exists = True
        else:
            exists = False
        return exists
    
    def __write_image(self, data):
        '''
        Helper function to save player profile image temporarily to disk.
        '''
        try:
            f = open('temp.png', 'wb')
            f.write(data)
        except IOError, e:
            print 'Error %d: %s' % (e.args[0], e.args[1])