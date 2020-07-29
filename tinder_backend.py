import mysql.connector
class TinderBackend:

    def __init__(self):
         self.conn=mysql.connector.connect(user="root",password="",host="localhost",database="tinder")
         self.mycursor=self.conn.cursor()

    def verifyuser(self,email,password):
        self.mycursor.execute(
            """SELECT * from `users` WHERE `email` LIKE '%s' and `password` LIKE '%s'""" % (email, password))
        user_list = self.mycursor.fetchall()
        c = 0
        for i in user_list:
            c = c + 1
            self.current_user_id = i[0]
        if c == 1:
           return i[1]
        else:
           return ""
    def adduser(self,name,email,password,gender,city):
        self.mycursor.execute(
            """INSERT into `users`(`name`,`email`,`password`,`gender`,`city`)VALUES('%s','%s','%s','%s','%s')""" % (
            name, email, password, gender, city))
        self.conn.commit()
    def view_all_users(self):
        self.mycursor.execute("""SELECT * from `users`""")
        user_list=self.mycursor.fetchall()
        return user_list
    def propose(self,juliet_id):
        self.mycursor.execute("""INSERT into `proposal`(`romeo_id`,`juliet_id`)VALUES('%s','%s')"""%(self.current_user_id,juliet_id))
        self.conn.commit()

    def view_sent_proposals(self):
        self.mycursor.execute(
        """SELECT * from`proposal` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`romeo_id`='%s'""" % (
            self.current_user_id))
        user_list = self.mycursor.fetchall()
        return user_list
    def view_recieved_proposal(self):
        self.mycursor.execute("""SELECT * from `proposal` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`juliet_id`='%s'"""%(self.current_user_id))
        user_list=self.mycursor.fetchall()
        return user_list
    def view_matches(self):
         self.mycursor.execute("""SELECT * from`proposal` p JOIN `users` u on p.`romeo_id`=u.`user_id` WHERE
         `juliet_id`='%s' AND `romeo_id` IN(SELECT `juliet_id`from `proposal` WHERE `romeo_id`='%s')"""%(self.current_user_id,self.current_user_id))
         user_list=self.mycursor.fetchall()
         return user_list



ob=TinderBackend()
