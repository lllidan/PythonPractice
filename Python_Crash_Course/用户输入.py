
# coding: utf-8

# In[ ]:


name = input("Please enter your name:")
print("Hello, " + name + "!")


# ### 通过在提示末尾包含一个空格，可将提示语用户输入分开，让用户清楚其输入始于何处

# In[2]:


Prompt = "If you tell us whos you are, we can personalize the message you see"
Prompt += "\nWhat is your first name?"

name = input(Prompt)
print("Hello， " + name + "!")


# In[3]:


height = input("How tall are you, in inches?")
height = int(height)

if height >= 36:
    print("\nYou're tall enought to ride!")
else:
    print("\nYou'll be able to ride when you're a little order")


# In[4]:


current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1


# In[7]:


prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != "quit":
        print(message)


# In[10]:


prompt = "\nPlease enter the name of a city you have visited:"
prompt = "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() +"!")


# # 使用while循环来处理列表和字典

# In[15]:


# 首先 ，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brain', 'candance']
confirmed_users = []

#验证每个用户，直到没有未验证用户为止
# 将每个经过验证的的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# ### 使用用户输入来填充字典

# In[25]:


responses = {}

# 设置一个标志， 指出调查是否继续
polling_active = True
while polling_active:
        # 提示输入被调查者的名字和回答
        name = input("\nWhat is your name? ")
        reponse = input("Which mountain would you like to climb someday? ")
        
        # 将答案存储在字典中
        responses[name] = reponse
        
        # 看看是否还有人要参与调查
        repeat = input("would you like to let another person respond? (yes/no)")
        if repeat == 'no':
            polling_active = False
            
# 调查结束， 显示结果
print("\n---Poll Results ---")
for name ,response in responses.items():
    print(name + " would like to climb " + response + ".")

