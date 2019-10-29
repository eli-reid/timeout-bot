import pandas as pd 
import mysql.connector as dbconnect
import json 

def main ():
   
    chatData=pd.DataFrame(data=pd.read_csv('ChatLog.csv'))
    chatDataStr=chatData['ChatMsg'].to_json(  )
    chatWordList=makeWordDictList(chatData['ChatMsg'].tolist())
    timeoutData=pd.DataFrame(data=pd.read_csv('ChatTimeout.csv'))
    timeoutWordList=makeWordDictList(timeoutData['Msgs'].tolist())
    return

def makeWordDictList(messageList):
    """    Input: 
                messageList (list) - list of messages (str)
           Returns: list of dictionaries {word:'word', subString:'wordBefore word wordAfter'}
           SubString length should be 1 to 3 depending on message
    """
    wordList=[]
    messageListLen=len(messageList)
    for i in range(messageListLen):
        percent=getPercent(i+1,messageListLen)
        words=str(messageList[i]).split()
        for j in range(len(words)):
          wordList.append({'word': words[j],'subString':" ".join(words[j-1:j+2] if j>0 else words[0:j+2])})
        print("Generating list of words and substrings: [{:25}] {:3.2f}%".format("*" * int(percent//4),percent),end="\r")  
    print()
    return wordList


def getPercent(dividend,divisor):
    """ 
        Input: 2 numbers int or float 
        Returns: float percent value   0.00 to 100.00 or -1 under error condition
    """
    try:
        return float((smallNum/largeNum)*100)
    except:
        return -1


if __name__ =="__main__":
    main()


                   