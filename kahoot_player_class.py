from selenium import webdriver
import random
import threading
from time import sleep




class Kahoot_Player:
    def __init__(self , kahoot_code,  name):
        self.kahoot_code = kahoot_code
        self.name = name
        self.quest_number = 1
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options = options)
        self.alive = True
        self.register()


    def matar(self):
        self.driver.close()
        self.alive = False
        print("Session Died for {}".format(self.name))

    def register(self):
        try:
            i = self.name
            self.driver.get("https://kahoot.it")
            sleep(1)

            print("logging {}".format(self.name))
            login = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[2]/main/div/form/input")
            login.send_keys(self.kahoot_code)
            sleep(2)
            enter = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[2]/main/div/form/button")
            enter.click()
            sleep(2)
            nickname = i
            nickname_box = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[2]/main/div/form/input").send_keys(nickname)
            okgo = self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[2]/main/div/form/button").click()
            print("created",  self.name)
        except:
            self.matar()

    def play_round(self):
        while (True):
            try:
                button_index = 1
                questions = list()
                while True:
                    try:
                        q = self.driver.find_element_by_xpath(f"/html/body/div/div[1]/main/div[2]/div/div/button[{button_index}]")
                        questions.append(q)
                        button_index += 1
                    except:
                        break
                resp = random.choice(questions)
                resp.click()
                print("answered {} , question:{}".format(self.name, self.quest_number))
                print("*"*50)
                self.quest_number += 1
                break
            except:
                sleep(0.1)

    def play(self):
        while(True):
            self.play_round()


class Kahoot_Master:
    def __init__(self, kahoot_code , n_tentacles , name):
        self.n_tentacles = int(n_tentacles)
        self.name = name
        self.kahoot_code = kahoot_code
        self.lista = self._name_list()

    def _name_list(self):
        lista = []
        for i in range(1,self.n_tentacles +1):
            lista.append("{}{}".format(self.name , i))
        return(lista)

    def tentacle(self , name):
        tentacle = Kahoot_Player(self.kahoot_code , name)
        tentacle.play()

    def parallel_tentacle(self):
        threads = []
        print("started")
        for i in self.lista:
            t = threading.Thread(target = self.tentacle , args = (i , ) , name = "thread{}".format(i))
            t.start()
            threads.append(t)
        for i in threads:
            i.join()
