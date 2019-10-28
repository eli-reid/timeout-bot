import pandas as pd
import mysql.connector as db

class bottrainer(object):
    """
    this class loads and calculatse chatdata to see if what is unapproriate for chatroom
    based on historic data of logged chat and timedout msgs
    takes a input of two data sets chat messages and timed out messages 
    returns a single data set of calculated percentages stored in a csv file based on frequancy of the word and a 3 word phrase (word before, word, word after) being timed out
    """

    def __init__(self):
         

        self.chatdata = pd.DataFrame()
        self.timeoutData = pd.DataFrame()
    
    def start():
        pass

    def _getDataFromDB(tableName,columnName,mySQLSetting):
        """
        get message data from mysql db
        input: tableName(str), columnName(str), mySQLSetting(dict)
        Output: pandas DataFrame
        Displays loading %
        """
       
        pass

    def chatMsgToStr(messages):
        """ 
            Input(list): list of messages
            Output(str): string of messages in csv form without punctuation 
        """
        pass

    
    def _getWordList():
        pass






