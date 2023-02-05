#made by harshdeep 100% #error free Tested more than 100 times don't mess with the files in folder
#if it don't know the answer it will ask you "what should be the answer of this question" and you'll have to type that answer in terminal to save it because this is in testing mode

#copy these command to install python required packages 
# pip install pyttsx3
# pip install SpeechRecognition
# pip install pyaudio
#pip install pywhatkit

#github account username - connectharsh
#linkedin link - https://www.linkedin.com/in/connectharsh/

import pyttsx3
import speech_recognition as s
sr = s.Recognizer() 
import pyautogui
speaker = pyttsx3.init()
import time
import pywhatkit as kit


#function recording the message
def record():
    try:
        with s.Microphone() as m:
            print('\n\n*************************************************************************************    listening   ****************************************************************************************** \n\n')
            voice = sr.listen(m, phrase_time_limit=3)
            if not voice == None and  not voice =='':
                voice_text = sr.recognize_google(voice,language='eng-in')
                voice_text = voice_text.lower()
                return voice_text
            else:
                return '90579057'    
    except:
        return '90589058'            


#stopping playing music
def stopIt():
    with pyautogui.hold('alt'):
                pyautogui.press('tab')
    time.sleep(2)            
    pyautogui.press('space')
    with pyautogui.hold('alt'):
                pyautogui.press('tab')


#this will close the current running program                
def closeIt():
    speak('is program opened in full mode')
    anss = record()
    anss = anss.split()
    if not anss =='90589058' and not anss == None:
        if 'yes in answer':
            with pyautogui.hold('alt'):
                pyautogui.press('tab')
            time.sleep(2)    
            pyautogui.moveTo(1350,5)
            pyautogui.click()
            pyautogui.moveTo(500,500)
        else:
            speak('sorry i cant close it for now')
    else: 
            speak('sorry i cant close it for now')            


#function speaking the message
def speak(message):
    voices = speaker.getProperty('voices')  
    speaker.setProperty('voice', voices[1].id) 
    rate = speaker.getProperty('rate')  
    speaker.setProperty('rate', 125)
    print(message)
    speaker.say(message)
    speaker.runAndWait()
    speaker.stop()



#initializing the old data 
def setQandA():
    comRes = True
    userRes = True
    lastUserRes = True
    lastCompRes = True
    with open('compRes.txt') as c:
        while comRes:
            comRes = c.readline()
            comRes = comRes.replace('\n','')
            ComputerResponseList.append(comRes)

    with open('userRes.txt') as u:
        while userRes:
            userRes = u.readline()
            userRes = userRes.replace('\n','')
            userResponseList.append(userRes)

    with open('lastUserRes.txt') as lu:
        while lastUserRes:
            lastUserRes = lu.readline()
            lastUserRes = lastUserRes.replace('\n','')
            lastUserResponseList.append(lastUserRes)
    with open('lastCompRes.txt') as lr:
        while lastCompRes:
            lastCompRes = lr.readline()
            lastCompRes = lastCompRes.replace('\n','')
            lastComputerResponseList.append(lastCompRes) 



    #removing last blank item from all lists         
    lastResInd = len(ComputerResponseList)-1
    last50ResInd = len(lastComputerResponseList)-1
    ComputerResponseList.remove(ComputerResponseList[lastResInd])
    userResponseList.remove(userResponseList[lastResInd])     
    lastComputerResponseList.remove(lastComputerResponseList[last50ResInd])
    lastUserResponseList.remove(lastUserResponseList[last50ResInd])


    # print(userResponseList)
    # print(ComputerResponseList)        
    # print(lastUserResponseList)
    # print(lastComputerResponseList)



#function to addanswer if i don't have the answer
def addAnswer(userRespp):
    speak('how should i answer this')
    userResToAdd = input('what should be the answer of this question\n')
    ComputerResponseList.append(userResToAdd)
    userResponseList.append(userRespp)
    finalReply('added successfully',userRespp)


#shutdown
def shutdown():
    with open('compRes.txt','w') as c:
        for finalCompRes in ComputerResponseList:
            c.write(f'{finalCompRes}\n')
    with open('userRes.txt','w') as u:
        for finalUserRes in userResponseList:
            u.write(f'{finalUserRes}\n')
    with open('lastUserRes.txt','w') as lu:
        for finalLastRes in lastUserResponseList:
            lu.write(f'{finalLastRes}\n')        
    with open('lastCompRes.txt','w') as lc:
        for finalCompRes in lastComputerResponseList:
            lc.write(f'{finalCompRes}\n')        
    finalReply('shutting down, have a nice day', 'shutdown')        
    exit()


#if i give wrong answer i can use this function to correct that answer
def improveAnswer():
    tempList = [item for item in lastUserResponseList]
    lastIndex = len(tempList)-2
    userRResp = tempList[lastIndex]
    tempIndex = userResponseList.index(userRResp)
    speak(f'what should be the answer of.. **{userRResp}**')
    improvedAnswer = record()
    if not improvedAnswer == '' and not improvedAnswer== None and not improvedAnswer =='\n' and not 'ignore' in improvedAnswer and not improvedAnswer=='90589058':
        ComputerResponseList[tempIndex] = improvedAnswer
        finalReply('answer improved','improve')
    else:
        finalReply('answer not improved','improve')




#sending whatsapp message using this
def sendMessage():
    phn = record()
    phn = phn.replace("-","")
    phn = phn.replace(" ", "")
    phn = "+91" + phn
    if len(phn)==13:
        speak("what is the message")
        print("recording the message...")
        msg = record() 
        if msg =='90589058':
            speak('message could not be blank')
        else:
            speak(f"sending {msg} to {phn}.. i will be back in 10 seconds..")
            kit.sendwhatmsg_instantly(phn,msg)

    else:
        speak("sorry darling... the message is not sent you can try again") 



#this is the final computer reply function
def finalReply(computerAnswer,userResponse):
    lastComputerResponseList.remove(lastComputerResponseList[0])
    lastUserResponseList.remove(lastUserResponseList[0])
    lastComputerResponseList.append(computerAnswer)
    lastUserResponseList.append(userResponse)
    speak(computerAnswer)
    
   
#playing music
def playMusic():
    speak('please tell me the music name more clearly')
    song = record()
    if not song  == None and not song == '90589058':
        kit.playonyt(song)
        time.sleep(4)
        with pyautogui.hold('alt'):
            pyautogui.press('tab')
    else:
        speak('song not played')    

#checking if the answer is in my data or not
def pleaseReply(userResp):
    global answerFound
    answerFound = False
    global tempUserResp    
    if userResp in userResponseList:
        tempInd = userResponseList.index(userResp)
        computerAnswer = ComputerResponseList[tempInd]
        finalReply(computerAnswer,userResp)    
    else:
        for uRes in userResponseList:
            if userResp in uRes:
                answerFound = True
                temporaryIndex = userResponseList.index(uRes)
                possibleReply = ComputerResponseList[temporaryIndex]
                userResponseList.append(userResp)
                ComputerResponseList.append(possibleReply)
                finalReply(possibleReply,userResp)
                break

        #removing some things from userresponse to check once again if answer in my data    
        tempUserResp = userResp.replace('please','')
        tempUserResp = userResp.replace('you','')
        tempUserResp = userResp.replace('do','')
        tempUserResp = userResp.replace('my','')
        tempUserResp = userResp.replace('what','')
        tempUserResp = userResp.replace('your','')
        tempUserResp = userResp.replace('who','')
        tempUserResp = userResp.replace('dear','')
        tempUserResp = userResp.replace('me','')
        tempUserResp = userResp.replace('darling','')
        tempUserResp = userResp.replace('baby','')
        tempUserResp = userResp.replace('google','')
        tempUserResp = userResp.replace('youtube','')        

        if not answerFound:
            if not tempUserResp == '':
                for uRRes in userResponseList:
                    if tempUserResp in uRRes:
                        answerFound = True
                        temporaryIndex = userResponseList.index(uRRes)
                        possibleReply = ComputerResponseList[temporaryIndex]
                        userResponseList.append(userResp)
                        ComputerResponseList.append(possibleReply)
                        finalReply(possibleReply,userResp)
                        break 
       
            else:
                addAnswer(userResp) #answer not found it will ask you to add it
        okayResp = tempUserResp.split()        
        if okayResp[0] == 'search':
            answerFound = True
            googleIt()        
        if okayResp[0] =='play':
            answerFound = True
            playMusic()                      
        elif not answerFound:
            addAnswer(userResp)   #answer not found it will ask you to add it     

#function to google
def googleIt():
    speak('please tell me what to search on google in clear words')
    toSearch = record()
    toSearch = toSearch.replace('please','')
    toSearch = toSearch.replace('search','')
    if not toSearch == None and not toSearch == '90589058':
        kit.search(toSearch)
    else:
        speak('google search ignored successfully')    


#if user has replied yes it will check if user want to run functions
def runIt():
    lastCompReplyInd = len(lastComputerResponseList)-1
    lastUserReplyInd = len(lastUserResponseList)-2
    lastCompReply = lastComputerResponseList[lastCompReplyInd]
    lastCompReply = lastCompReply.replace('\n','')
    # print(lastCompReply)
    lastUserReply = lastUserResponseList[lastUserReplyInd]

    if lastCompReply =='do you want me to play music?':
        playMusic()

    elif lastCompReply =='do you want me to send a whatsapp message?':
        sendMessage() 

    elif lastCompReply == 'do you want me to google search it?':
        googleIt()   

    elif lastCompReply == 'do you want me to shut down?':
        shutdown()

    elif lastCompReply == 'do you want me to improve my answer?':
        improveAnswer()   
    elif lastCompReply =='do you want me to stop it?':
        stopIt()     
    elif lastCompReply =='do you want me to close it?':
        closeIt()         
    elif lastCompReply =='do you want me to tell the time?':
        currTime = time.strftime('%H:%S')
        speak(f'the time is {currTime}')    
    else:
        pleaseReply(lastUserReply)    



#checking if user had replied yes
def checkReply(userRes):
    if userRes == '90589058':
        print('extreme silence')
    else:
        splitUserRes = userRes.split()
        if splitUserRes[0]=='yes':
            runIt()
        else:
            pleaseReply(userRes)    



if __name__ == "__main__":

    #setting up user and computer responses
    userResponseList = []
    ComputerResponseList= []
    lastUserResponseList = []
    lastComputerResponseList= []
    setQandA()

    #starting the darling ****the main code**** unstoppable darling 3.0
    try:

        hour = int(time.strftime('%H'))
        global greetings
        if hour>=4 and hour<12:
            greetings = 'good morning'
        elif hour>=12 and hour<18:
            greetings = 'good afternoon'
        elif hour>=18 and hour<24:
            greetings = 'good evening'    

        speak(f'hello dear, {greetings}.... darling is back again ')
        while True:
            userResponse = record()
            checkReply(userResponse)
    except Exception as e:
        print(e)
        speak('sorry to say that there is some kind of error, or your internet connnection is off i will have to shut down... by have a nice day')
    finally:
        exit()
