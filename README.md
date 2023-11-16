#TASK 1 SOFTWARE CONFIGURATION


*Subtask 1 Why did you choose to participate in this challenge?*


I have recently embarked on a personal journey to pursue a career as a software tester, a goal that has been in my mind for quite some time. Throughout my professional experience, I have utilized various platforms to assess the suitability of a career as a software tester, and these experiences have only reinforced my belief that this is the right path for me. I have acquired a diverse set of skills that are highly applicable to the role. Notably, I have acquired keen attention to detail, particularly in the exploration of new software and understanding its functionality. Additionally, I have actively participated in the Dare IT Manual Tester challenge and have found immense enjoyment in tackling each challenge presented to me.


*Subtask 4 Quick ISTQB knowledge test [ISTQB](https://getistqb.com/quiz-purpurowy/)*

![Image 16-11-2023 at 10 36](https://github.com/AgataSzafranek/AT_challenge/assets/142822653/95067e3c-d341-4c1c-86d0-afeb85728058)

#TASK 2 SELECTORS

*Subtask 2 Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.*


[Scouts panel](https://scouts-test.futbolkolektyw.pl/en/login?redirected=true)


👉 Header xpath


1. //*[@id="__next"]/form/div/div[1]/h5


2. //*[text()="Scouts Panel"]


3. //h5


👉 Login field xpath


1. //*[@id="login"]


2. //*[text()="Login"]


3. //input[@name="login"]


👉 Password field xpath


1. //*[@id="password"]


2. //input[@name="password"]


3. //form/div/div/div[2]/div/input


👉 Remind Password xpath


1. //*[@id="__next"]/form/div/div[1]/a


2. //*[text()="Remind password"]


3. //child::div/a


👉 Language option xpath


1. //*[@id="__next"]/form/div/div[2]/div/div


2. //*[text()="English"]


3. //*[contains(@class,"MuiSelect-root MuiSelect-select")]


👉 Sign in xpath


1. //*[@id="__next"]/form/div/div[2]/div/div


2. //*[text()="Sign in"]


3. //*[contains(@class,"MuiButton-l")]
