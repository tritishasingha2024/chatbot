import google.generativeai as genai

def main():
  inp=input("You: ")
  genai.configure(api_key="AIzaSyDo_7-r5JaFi-reoPa9bDlaN9gDOzA7yxg")
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(inp)
  print("Bot:",response.text)

i=1
loop=0
while(i!=0):
    if(loop==0):
       print("Welcome To Chat Bot")
       loop=loop+1
    main()